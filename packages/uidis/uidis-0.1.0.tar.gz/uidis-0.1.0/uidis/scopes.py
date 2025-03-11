from __future__ import annotations
from collections.abc import Iterable
from msgspec import Struct
from .icons import Icon


class Item(Struct, array_like=True, tag=False):
    label: str
    path: str
    icon: int | None = None


class Scope(Struct, array_like=True, tag=False):
    label: str
    items: list[Item | Scope]
    icon: int | None = None

    def item(self, label: str, path: str, icon: Icon | None = None) -> Item:
        return Item(label, path, None if icon is None else icon.code)

    def scope(self, label: str, items: Iterable[Item | Scope] = (), icon: Icon | None = None) -> Scope:
        return Scope(label, list(items), None if icon is None else icon.code)


def item(label: str, path: str, icon: Icon | None = None) -> Item:
    return Item(label, path, None if icon is None else icon.code)


def scope(label: str, items: Iterable[Item | Scope] = (), icon: Icon | None = None) -> Scope:
    return Scope(label, list(items), None if icon is None else icon.code)
