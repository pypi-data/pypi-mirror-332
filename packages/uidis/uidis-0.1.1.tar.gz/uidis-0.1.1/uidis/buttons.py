from .layout import UI

__all__ = ("Link", "Submit")


class Link(UI):
    href: str
    label: str = ""
    external: bool = False


class Submit(UI):
    value: str = "Submit"
    name: str = "submit"
