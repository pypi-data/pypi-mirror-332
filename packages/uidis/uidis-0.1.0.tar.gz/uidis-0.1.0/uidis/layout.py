from __future__ import annotations
from collections.abc import Iterable, Iterator
from functools import cache
from itertools import chain
from typing import TYPE_CHECKING

from .lookups import Lookup

from .enums import Color, Spacing
from .shared import iter_size_optimised_ids
from msgspec import Struct
from msgspec.structs import replace

if TYPE_CHECKING:
    from .text import Text
else:
    Text = Struct

UILookup = Lookup.new("ui")
_iter_tags: chain[int] = iter(iter_size_optimised_ids())


def ui_tagger(qualname: str) -> int:
    UILookup[f"{qualname.split('.')[-1]}"] = (tag := next(_iter_tags))
    return tag


@cache
def _gettext() -> type[Text]:
    from .text import Text

    return Text


class UI(Struct, kw_only=True, array_like=True, tag=ui_tagger):
    def __iter__(self) -> Iterator[str]:
        return iter(self.render())

    def render(self) -> Iterable[str]:
        raise NotImplementedError(f"{self.__class__.__qualname__} does not implement .render()")

    def __bytes__(self) -> bytes:
        return b"".join(map(str.encode, self.render()))

    def __html__(self) -> str:
        return "".join(self.render())

    def __or__(self, other: UI | str | Spacing) -> UI:
        match other:
            case UI():
                return Inline(content=(self, other))
            case Spacing():
                return Inline(content=(self,), justify=other)
            case str():
                return Inline(content=(self, _gettext()(text=other)))
            case _:
                raise TypeError(f"Cannot Inline {type(other)} and {type(self)}")

    def __ror__(self, other: str | Spacing) -> UI:
        match other:
            case Spacing():
                return replace(self, justify=other)
            case str():
                return Inline(content=(_gettext()(text=other), self))
            case _:
                raise TypeError(f"Cannot Inline {type(other)} and {type(self)}")


class Inline(UI):
    content: Iterable[UI]
    justify: Spacing = Spacing.SpaceBetween
    align: Spacing = Spacing.Center
    color: Color = Color.Default

    def __or__(self, other: UI | str | Spacing) -> Inline:
        match other:
            case Inline():
                return replace(self, content=(*self.content, *other.content))
            case UI():
                return replace(self, content=(*self.content, other))
            case Spacing():
                return replace(self, justify=other)
            case str():
                return replace(self, content=(*self.content, _gettext()(text=other)))
            case _:
                raise TypeError(f"Cannot Inline {type(other)} and {type(self)}")

    def __ror__(self, other: str | Spacing) -> Inline:
        match other:
            case Spacing():
                return replace(self, justify=other)
            case str():
                return replace(self, content=(_gettext()(text=other), *self.content))
            case _:
                raise TypeError(f"Cannot Inline {type(other)} and {type(self)}")


class Card(UI):
    content: Iterable[UI]
    color: Color = Color.Default
