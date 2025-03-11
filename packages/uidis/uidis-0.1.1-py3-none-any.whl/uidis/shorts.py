from .enums import Color, Spacing
from .icons import IconRepo
from .layout import UI, Card, Inline
from .text import Text, Title

icons = IconRepo()


def card(*rows: UI | str, color: Color = Color.Default) -> Card:
    return Card(
        content=(Text(row) if isinstance(row, str) else row for row in rows),
        color=color,
    )


def inline(
    *content: UI | str,
    justify: Spacing = Spacing.SpaceBetween,
    align: Spacing = Spacing.Center,
    color: Color = Color.Default,
) -> Inline:
    return Inline(
        content=(Text(column) if isinstance(column, str) else column for column in content),
        justify=justify,
        align=align,
        color=color,
    )


def text(text: str, color: Color = Color.Default) -> Text:
    return Text(text=text, color=color)


def h6(text: str, color: Color = Color.Default) -> Title:
    return Title(text=text, level=6, color=color)


def h5(text: str, color: Color = Color.Default) -> Title:
    return Title(text=text, level=5, color=color)


def h4(text: str, color: Color = Color.Default) -> Title:
    return Title(text=text, level=4, color=color)


def h3(text: str, color: Color = Color.Default) -> Title:
    return Title(text=text, level=3, color=color)


def h2(text: str, color: Color = Color.Default) -> Title:
    return Title(text=text, level=2, color=color)


def h1(text: str, color: Color = Color.Default) -> Title:
    return Title(text=text, level=1, color=color)
