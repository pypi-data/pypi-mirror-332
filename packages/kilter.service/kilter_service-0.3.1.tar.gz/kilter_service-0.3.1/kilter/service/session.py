# Copyright 2022-2025 Dominik Sekotill <dom.sekotill@kodo.org.uk>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Sessions are the kernel of a filter, providing it with an async API to access messages
"""

from __future__ import annotations

from collections.abc import AsyncGenerator
from collections.abc import AsyncIterator
from collections.abc import Sequence
from contextvars import ContextVar
from dataclasses import dataclass
from enum import Enum
from ipaddress import IPv4Address
from ipaddress import IPv6Address
from pathlib import Path
from types import TracebackType
from typing import AsyncContextManager
from typing import Literal
from typing import Protocol
from typing import TypeAlias
from warnings import warn

from typing_extensions import Self

from ..protocol.core import EditMessage
from ..protocol.core import EventMessage
from ..protocol.messages import *
from . import util

FilterResponse: TypeAlias = Accept | Reject | Discard | ReplyCode


class Aborted(BaseException):
	"""
	An exception for aborting filters on receipt of an Abort message
	"""


class Filter(Protocol):
	"""
	Filters are callables that accept a `Session` and return a response
	"""

	async def __call__(self, session: Session, /) -> FilterResponse: ...  # noqa: D102


class Sender(Protocol):
	"""
	Senders asynchronously handle sending messages with their "send" method
	"""

	async def send(self, message: EditMessage) -> None: ...  # noqa: D102


class Phase(int, Enum):
	"""
	Session phases indicate what messages to expect and are impacted by received messages

	Users should not generally need to use these values, however an understanding of the
	state-flow they represent is useful for understanding some error exception
	raised by `Session` methods.
	"""

	INIT = 0
	"""
	This phase is the pre-connected phase of a session; this phase will be completed before
	users see the session object.
	"""

	CONNECT = 1
	"""
	This phase is the starting phase of a session, during which a HELO/EHLO message may be
	awaited with `Session.helo()`.
	"""

	MAIL = 2
	"""
	This phase is entered after HELO/EHLO, during which a MAIL message may be awaited with
	`Session.envelope_from()`.  The `Session.extension()` method may also be used to get
	the raw MAIL command with any extension arguments, or any other extension commands
	that the MTA does not support (if the MTA supports passing these commands to
	a filter).
	"""

	ENVELOPE = 3
	"""
	This phase is entered after MAIL, during which any RCPT commands may be awaited with
	`Session.envelope_recipients()`.  The `Session.extension()` method may also be used to
	get the raw RCPT command with any extension arguments, or any other extension commands
	that the MTA does not support (if the MTA supports passing these commands to
	a filter).
	"""

	HEADERS = 4
	"""
	This phase is entered after a DATA command, while message headers are processed.
	Headers may be iterated as they arrive, or be collected for later through the
	`Session.headers` object.
	"""

	BODY = 5
	"""
	This phase is entered after a message's headers have been processed.  The raw message
	body may be iterated over in chunks through the `Session.body` object.
	"""

	POST = 6
	"""
	This phase is entered once a message's body has been completed (or skipped).  During
	this phase the message editing methods of a `Session` object or the `Session.headers`
	and `Session.body` objects may be used.
	"""


@dataclass
class Position:
	"""
	A base class for `Before` and `After`, this class is not intended to be used directly
	"""

	subject: Header|Literal["start"]|Literal["end"]


@dataclass
class Before(Position):
	"""
	Indicates a relative position preceding a subject `Header` in a header list

	See `HeadersAccessor.insert`.
	"""

	subject: Header


@dataclass
class After(Position):
	"""
	Indicates a relative position following a subject `Header` in a header list

	See `HeadersAccessor.insert`.
	"""

	subject: Header


START = Position("start")
"""
Indicates the start of a header list, before the first (current) header
"""

END = Position("end")
"""
Indicates the end of a header list, after the last (current) header
"""


class Session:
	"""
	The kernel of a filter, providing an API for filters to access messages from an MTA
	"""

	host: str
	"""
	A hostname from a reverse address lookup performed when a client connects

	If no name is found this value defaults to the standard presentation format for
	`Session.address` surrounded by "[" and "]", e.g. "[192.0.2.100]"
	"""

	address: IPv4Address|IPv6Address|Path|None
	"""
	The address of the connected client, or None if unknown
	"""

	port: int
	"""
	The port of the connected client if applicable, or 0 otherwise
	"""

	macros: dict[str, str]
	"""
	A mapping of string replacements sent by the MTA

	See `smfi_getsymval <https://pythonhosted.org/pymilter/milter_api/smfi_getsymval.html>`_
	from `libmilter` for more information.

	Warning:
		The current implementation is very naïve and does not behave exactly like
		`libmilter`, nor is it very robust.  It will definitely change in the future.
	"""

	headers: HeadersAccessor
	"""
	A `HeadersAccessor` object for accessing and modifying the message header fields
	"""

	body: BodyAccessor
	"""
	A `BodyAccessor` object for accessing and modifying the message body
	"""

	def __init__(
		self,
		sender: Sender,
		broadcast: util.Broadcast[EventMessage]|None = None,
	):
		self.host = ""
		self.address = None
		self.port = 0

		self.sender = sender
		self.broadcast = broadcast or util.Broadcast[EventMessage]()

		self.macros = dict[str, str]()
		self.headers = HeadersAccessor(self, sender)
		self.body = BodyAccessor(self, sender)

		# Phase checking is a bit fuzzy as a filter may not request every message,
		# so some phases will be skipped; checks should not try to exactly match a phase.
		self.phase = Phase.INIT

		self._helo: Helo|None = None

	async def __aenter__(self) -> Self:
		await self.broadcast.__aenter__()
		return self

	async def __aexit__(self, *_: object) -> None:
		await self.broadcast.__aexit__(None, None, None)
		# on session close, wake up any remaining deliver() awaitables
		await self.broadcast.shutdown_hook()

	def _reset(self) -> None:
		self.headers = HeadersAccessor(self, self.sender)
		self.body = BodyAccessor(self, self.sender)

	async def deliver(self, message: EventMessage) -> type[Continue]|type[Skip]:
		"""
		Deliver a message (or its contents) to a task waiting for it
		"""
		match message:
			case Connect():
				self.host = message.hostname
				self.address = message.address
				self.port = message.port
				async with self.broadcast:
					self.phase = Phase.CONNECT
				return Continue
			case Macro():
				self.macros.update(message.macros)
				return Continue  # not strictly necessary, but type checker needs something
			case Abort():
				async with self.broadcast:
					self.phase = Phase.CONNECT
				await self.broadcast.abort(Aborted)
				self._reset()
				return Continue
			case Helo():
				phase = Phase.MAIL
			case EnvelopeFrom() | EnvelopeRecipient() | Unknown():
				phase = Phase.ENVELOPE
			case Data() | Header():
				phase = Phase.HEADERS
			case EndOfHeaders() | Body():
				phase = Phase.BODY
			case EndOfMessage():  # pragma: no-branch
				phase = Phase.POST
		async with self.broadcast:
			self.phase = phase  # phase attribute must be modified in locked context
		await self.broadcast.send(message)
		return Skip if self.phase == Phase.BODY and self.body.should_skip() else Continue

	async def helo(self) -> str:
		"""
		Wait for a HELO/EHLO message and return the client's claimed hostname
		"""
		if self.phase > Phase.CONNECT:
			raise RuntimeError(
				"Session.helo() must be awaited before any other async features of a "
				"Session",
			)
		if self._helo:
			return self._helo.hostname
		while self.phase <= Phase.CONNECT:
			message = await self.broadcast.receive()
			if isinstance(message, Helo):
				self._helo = message
				return message.hostname
		raise RuntimeError("HELO/EHLO event not received")

	async def envelope_from(self) -> str:
		"""
		Wait for a MAIL command message and return the sender identity

		Note that if extensions arguments are wanted, users should use `Session.extension()`
		instead with a name of ``"MAIL"``.
		"""
		if self.phase > Phase.MAIL:
			raise RuntimeError(
				"Session.envelope_from() may only be awaited before the ENVELOPE phase",
			)
		while self.phase <= Phase.MAIL:
			message = await self.broadcast.receive()
			if isinstance(message, EnvelopeFrom):
				return bytes(message.sender).decode()
		raise RuntimeError("MAIL event not received")

	async def envelope_recipients(self) -> AsyncIterator[str]:
		"""
		Wait for RCPT command messages and iteratively yield the recipients' identities

		Note that if extensions arguments are wanted, users should use `Session.extension()`
		instead with a name of ``"RCPT"``.
		"""
		if self.phase > Phase.ENVELOPE:
			raise RuntimeError(
				"Session.envelope_from() may only be awaited before the HEADERS phase",
			)
		while self.phase <= Phase.ENVELOPE:
			message = await self.broadcast.receive()
			if isinstance(message, EnvelopeRecipient):
				yield bytes(message.recipient).decode()

	async def extension(self, name: str) -> memoryview:
		"""
		Wait for the named command extension and return the raw command for processing
		"""
		if self.phase > Phase.ENVELOPE:
			raise RuntimeError(
				"Session.extension() may only be awaited before the HEADERS phase",
			)
		bname = name.encode("utf-8")
		while self.phase <= Phase.ENVELOPE:
			message = await self.broadcast.receive()
			match message:
				case Unknown():
					if message.content[:len(bname)] == bname:
						assert isinstance(message.content, memoryview)
						return message.content
				# fake buffers for MAIL and RCPT commands
				case EnvelopeFrom() if name == "MAIL":
					vals = [b"MAIL FROM", message.sender, *message.arguments]
					return memoryview(b" ".join(vals))
				case EnvelopeRecipient() if name == "RCPT":
					vals = [b"RCPT TO", message.recipient, *message.arguments]
					return memoryview(b" ".join(vals))
		raise RuntimeError(f"{name} event not received")

	async def change_sender(self, sender: str, args: str = "") -> None:
		"""
		Move onto the `Phase.POST` phase and instruct the MTA to change the sender address
		"""
		await _until_editable(self)
		await self.sender.send(ChangeSender(sender, args or None))

	async def add_recipient(self, recipient: str, args: str = "") -> None:
		"""
		Move onto the `Phase.POST` phase and instruct the MTA to add a new recipient address
		"""
		await _until_editable(self)
		await self.sender.send(
			AddRecipientPar(recipient, args) if args else AddRecipient(recipient),
		)

	async def remove_recipient(self, recipient: str) -> None:
		"""
		Move onto the `Phase.POST` phase and instruct the MTA to remove a recipient address
		"""
		await _until_editable(self)
		await self.sender.send(RemoveRecipient(recipient))


class HeadersAccessor(AsyncContextManager["HeaderIterator"]):
	"""
	A class that allows access and modification of the message headers sent from an MTA

	To access headers (which are only available iteratively), use an instance as an
	asynchronous context manager; a `HeaderIterator` is returned when the context is
	entered.
	"""

	def __init__(self, session: Session, sender: Sender):
		self.session = session
		self.sender = sender
		self._table = list[Header]()
		self._aiter = ContextVar[HeaderIterator|None]("header-iter")

	async def __aenter__(self) -> HeaderIterator:
		if not (aiter := self._aiter.get(None)):
			aiter = HeaderIterator(self.__aiter())
			self._aiter.set(aiter)
		return aiter

	async def __aexit__(self, *_: object) -> None:
		if aiter := self._aiter.get():
			await aiter.aclose()
		self._aiter.set(None)

	async def __aiter(self) -> AsyncGenerator[Header, None]:
		# yield from cached headers first; allows multiple tasks to access the headers
		# in an uncoordinated manner; note the broadcaster is locked at this point
		for header in self._table:
			yield header
		seen = set(id(header) for header in self._table)
		while self.session.phase <= Phase.HEADERS:
			match (await self.session.broadcast.receive()):
				case Header() as header:
					header.freeze()
					self._table.append(header)
					seen.add(id(header))
					try:
						yield header
					except GeneratorExit:
						await self.collect()
						raise
				case EndOfHeaders():
					return
		# It's possible for collect() to have been called while yielded, in which case the
		# loop will end. Yield any headers that were stored by collect() but not yet
		# yielded.
		for header in self._table:
			if id(header) not in seen:
				yield header

	async def collect(self) -> None:
		"""
		Collect all headers without producing an iterator

		Calling this method before the `Phase.BODY` phase allows later processing of headers
		(after the HEADER phase) without the need for an empty loop.
		"""
		# note the similarities between this and __aiter; the difference is no mutex or
		# yields
		while self.session.phase <= Phase.HEADERS:
			match (await self.session.broadcast.receive()):
				case Header() as header:
					header.freeze()
					self._table.append(header)
				case _:
					return

	async def delete(self, header: Header) -> None:
		"""
		Move onto the `Phase.POST` phase and Instruct the MTA to delete the given header
		"""
		await self.collect()
		await _until_editable(self.session)
		index = _index_by_name(self._table, header)
		await self.sender.send(ChangeHeader(index, header.name, b""))
		self._table.remove(header)

	async def update(self, header: Header, value: bytes) -> None:
		"""
		Move onto the `Phase.POST` phase and Instruct the MTA to modify the value of a header
		"""
		await self.collect()
		await _until_editable(self.session)
		index = _index_by_name(self._table, header)
		await self.sender.send(ChangeHeader(index, header.name, value))
		index = self._table.index(header)
		self._table[index].value = value

	async def insert(self, header: Header, position: Position) -> None:
		"""
		Move onto the `Phase.POST` phase and instruct the MTA to insert a new header

		The header is inserted at `START`, `END`, or a relative position with `Before` and
		`After`; for example ``Before(Header("To", "test@example.com"))``.
		"""
		await self.collect()
		await _until_editable(self.session)
		match position:
			case Position(subject="start"):
				index = 0
			case Position(subject="end"):
				index = len(self._table)
			case Before():
				index = self._table.index(position.subject)
			case After():  # pragma: no-branch
				index = self._table.index(position.subject) + 1
			case _:
				raise TypeError("Expect a Position")
		if index >= len(self._table):
			await self.sender.send(AddHeader(header.name, header.value))
			self._table.append(header)
		else:
			await self.sender.send(InsertHeader(index + 1, header.name, header.value))
			self._table.insert(index, header)


class HeaderIterator(AsyncGenerator[Header, None]):
	"""
	Iterator for headers obtained by using a `HeadersAccessor` as a context manager
	"""

	def __init__(self, aiter: AsyncGenerator[Header, None]):
		self._aiter = aiter

	def __aiter__(self) -> Self:
		return self

	async def __anext__(self) -> Header:  # noqa: D102
		return await self._aiter.__anext__()

	async def asend(self, value: None = None) -> Header:  # noqa: D102
		return await self._aiter.__anext__()

	async def athrow(  # noqa: D102
		self,
		e: type[BaseException]|BaseException,
		m: object = None,
		t: TracebackType|None = None, /,
	) -> Header:
		if isinstance(e, type):
			return await self._aiter.athrow(e, m, t)
		assert m is None
		return await self._aiter.athrow(e, m, t)

	async def aclose(self) -> None:  # noqa: D102
		await self._aiter.aclose()

	async def restrict(self, *names: str) -> AsyncIterator[Header]:
		"""
		Return an asynchronous generator that filters headers by name
		"""
		async for header in self._aiter:
			if header.name in names:
				yield header


class BodyAccessor(AsyncContextManager[AsyncIterator[memoryview]]):
	"""
	A class that allows access and modification of the message body sent from an MTA

	To access chunks of a body (which are only available iteratively), use an instance as an
	asynchronous context manager; an asynchronous iterator is returned when the context is
	entered.
	"""

	def __init__(self, session: Session, sender: Sender):
		self.session = session
		self.sender = sender
		self._entered = 0
		self._skip = False
		self._aiter = ContextVar[AsyncGenerator[memoryview, None] | None]("body-iter")

	async def __aenter__(self) -> AsyncIterator[memoryview]:
		if not (aiter := self._aiter.get(None)):
			aiter = self.__aiter()
			self._aiter.set(aiter)
		self._entered += 1
		return aiter

	async def __aexit__(self, *_: object) -> None:
		if aiter := self._aiter.get(None):
			await aiter.aclose()
		self._aiter.set(None)
		self._entered -= 1

	async def __aiter(self) -> AsyncGenerator[memoryview, None]:
		while self.session.phase <= Phase.BODY:
			match (await self.session.broadcast.receive()):
				case Body() as body:
					assert isinstance(body.content, memoryview)
					yield body.content
				case EndOfMessage() as eom:
					assert isinstance(eom.content, memoryview)
					yield eom.content

	def should_skip(self) -> bool:
		"""
		Return whether the message body should be skipped

		The body should be skipped when there are no active contexts.  All correctly
		implemented filters should have started a context before the first `Body` message.

		Once this method returns `True` it becomes "locked in" and will always return `True`
		after.
		"""
		if self._skip:
			return True
		self._skip = self._entered == 0
		return self._skip

	async def write(self, chunk: bytes) -> None:
		"""
		Request that chunks of a new message body are sent to the MTA

		This method should not be called from within the scope created by using it's
		instance as an async context (`async with`); doing so may cause a warning to be
		issued and the rest of the message body to be skipped.
		"""
		if self._aiter.get(None):
			warn(
				"it looks as if BodyAccessor.write() was called on an instance from within "
				"it's own async context",
				stacklevel=2,
			)
		await _until_editable(self.session)
		await self.sender.send(ReplaceBody(chunk))


async def _until_editable(session: Session) -> None:
	if session.phase == Phase.POST:
		return
	while session.phase < Phase.POST:
		if session.phase == Phase.HEADERS:
			await session.headers.collect()
		else:
			await session.broadcast.receive()


def _index_by_name(table: Sequence[Header], needle: Header) -> int:
	index = 0
	name = needle.name.lower()
	for header in table:
		if header == needle:
			return index + 1
		if header.name.lower() == name:
			index += 1
	raise ValueError(f"header not found: {needle}")
