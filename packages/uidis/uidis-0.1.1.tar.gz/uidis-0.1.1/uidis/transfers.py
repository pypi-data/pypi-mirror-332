from enum import IntEnum
from msgspec import Struct
from .layout import UI


class DataTypes(IntEnum):
    PlainText = 0
    URIs = 2
    Bytes = 1


class String(Struct, tag=DataTypes.PlainText):
    value: str


class URIs(Struct, tag=DataTypes.URIs):
    value: list[str]


class Bytes(Struct, tag=DataTypes.Bytes):
    value: bytes


class Transfers(UI):
    content: UI
    data: UI
