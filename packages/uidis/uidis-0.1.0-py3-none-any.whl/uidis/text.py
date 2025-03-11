from typing import Annotated

from msgspec import Meta

from .enums import Color
from .layout import UI


class Title(UI):
    text: str
    level: Annotated[int, Meta(ge=1, le=6)] = 1
    color: Color = Color.Default


class Text(UI):
    text: str
    color: Color = Color.Default
