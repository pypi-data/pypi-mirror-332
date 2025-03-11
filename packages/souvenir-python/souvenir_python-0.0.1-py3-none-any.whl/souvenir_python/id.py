import os
from typing import Protocol, Type
import uuid

from souvenir_python.base32 import decode, encode

# Based off of the repo: https://github.com/j5pr/souvenir


class PrefixType(Protocol):
    @staticmethod
    def prefix() -> str:
        return ""


class Id:
    """
    ID class: stores 16 bytes plus a type prefix.
    """

    def __init__(self, prefix_type: Type[PrefixType], data: bytes):
        if len(data) != 16:
            raise ValueError("data must be 16 bytes")

        prefix = prefix_type.prefix()

        if not prefix or not prefix.isalnum():
            raise ValueError("prefix must be non-empty alphanumeric string")

        self.prefix = prefix
        self.data = data

    def __str__(self) -> str:
        return f"{self.prefix}_{encode(self.data)}"

    def bytes(self) -> bytes:
        return self.data

    def uuid(self) -> uuid.UUID:
        return uuid.UUID(bytes=self.data)


def zero_id(prefix_type: Type[PrefixType]) -> Id:
    """Returns an ID with 16 zero bytes."""
    return Id(prefix_type, bytes(16))


def new_id(prefix_type: Type[PrefixType], data: bytes) -> Id:
    """Generates a new ID."""
    return Id(prefix_type, data)


def random_id(prefix_type: Type[PrefixType]) -> Id:
    """Generates a new random ID."""
    return Id(prefix_type, os.urandom(16))


def parse_id(prefix_type: Type[PrefixType], s: str) -> Id:
    """
    Parses an ID from its string representation.
    The string must be of the form "prefix_encodedData".
    """
    prefix = prefix_type.prefix()

    parts = s.split("_", 1)
    if len(parts) != 2 or parts[0] != prefix:
        raise ValueError("prefix mismatch or invalid format")
    decoded = decode(parts[1])
    return Id(prefix_type, decoded)


def parse_uuid(prefix_type: Type[PrefixType], u: uuid.UUID) -> Id:
    """Converts a Python uuid.UUID into an ID."""
    return Id(prefix_type, u.bytes)


def cast_id(id_obj: Id, new_prefix_type: Type[PrefixType]) -> Id:
    """
    "Casts" the ID to a new type by simply replacing its prefix,
    while keeping the underlying 16 bytes intact.
    """
    return Id(new_prefix_type, id_obj.data)
