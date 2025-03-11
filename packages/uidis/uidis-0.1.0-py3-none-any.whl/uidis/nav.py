from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator
from itertools import count

from msgspec import Struct

from .icons import Icon
from .shared import pack


class Item(Struct):
    label: str
    path: str
    icon: Icon | None = None


class Scope(Struct):
    label: str
    icon: Icon | None = None
    scopes: Iterable[Scope] = ()
    items: Iterable[Item] = ()

    @property
    def pack(self):
        return pack(tuple(NavPackage.pack(self)))


class NavLink(Struct, tag=False, array_like=True):
    label: str
    path: str
    icon: int | None


class NavPackage(Struct, tag=False, array_like=True):
    index: int
    label: str
    icon: int | None
    parent: int | None
    children: list[int]
    links: tuple[NavLink, ...]

    @classmethod
    def pack(
        cls,
        scope: Scope,
        parent_index: int | None = None,
        add_to_parent: Callable[[int], None] = lambda _: None,
        i: Iterator[int] | None = None,
    ) -> Iterable[NavPackage]:
        i = i or iter(count(-32))
        index: int = next(i)
        add_to_parent(index)
        children: list[int] = []
        yield cls(
            index,
            scope.label,
            scope.icon and scope.icon.code,
            parent_index,
            children,
            tuple(NavLink(link.label, link.path, link.icon and link.icon.code) for link in scope.items),
        )
        for scope in scope.scopes:
            yield from cls.pack(scope, index, children.append, i)
