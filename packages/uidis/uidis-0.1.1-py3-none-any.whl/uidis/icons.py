from __future__ import annotations
from enum import IntEnum
from typing import ClassVar

from msgspec.structs import replace

from .layout import UI
from .lookups import Lookups


IconLookup = Lookups["icon"]

__all__ = ("Icon", "IconRepo")


class IconStyle(IntEnum):
    Outlined = 1
    Rounded = 2
    Sharp = 3


class Icon(UI):
    code: int
    style: IconStyle | None = None

    @property
    def outlined(self) -> Icon:
        return replace(self, style=IconStyle.Outlined)

    @property
    def sharp(self) -> Icon:
        return replace(self, style=IconStyle.Sharp)

    @property
    def rounded(self) -> Icon:
        return replace(self, style=IconStyle.Rounded)

    @property
    def default(self) -> Icon:
        return replace(self, style=None)


class IconRepo:
    __slots__: tuple[()] = ()

    _instance: ClassVar[IconRepo]

    def __new__(cls) -> IconRepo:
        if not (inst := getattr(cls, "_instance", None)):
            cls._instance = inst = super().__new__(cls)
        return inst

    def __getattr__(self, name: str) -> Icon:
        try:
            return Icon(IconLookup[name])
        except KeyError:
            raise AttributeError(f"No Icon named {name!r}")

    __call__ = __getitem__ = __getattr__
