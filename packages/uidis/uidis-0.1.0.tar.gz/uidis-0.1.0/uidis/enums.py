from enum import IntEnum
from typing import TYPE_CHECKING

from msgspec.structs import replace

if TYPE_CHECKING:
    from .layout import UI
else:
    UI = type


class Spacing(IntEnum):
    Start = 0
    Center = 1
    End = 2
    SpaceAround = 3
    SpaceBetween = 4
    SpaceEvenly = 5


class Color(IntEnum):
    Default = 0
    Primary = 1
    Secondary = 2
    Tertiary = 3
    Error = 4

    def __call__[UIType: UI](self, ui: UIType) -> UIType:
        return replace(ui, color=self)


class InputType(IntEnum):
    Text = 0
    Password = 1
    Email = 2
    Number = 3
    Date = 4
    Time = 5
    DateTime = 6
    Checkbox = 7
    Radio = 8
    Range = 9
    Color = 10
    File = 11
    Hidden = 12
