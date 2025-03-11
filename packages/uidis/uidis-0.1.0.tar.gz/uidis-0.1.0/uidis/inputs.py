from .enums import InputType
from .layout import UI


class Input(UI):
    name: str
    value: str = ""
    type: InputType = InputType.Text
    placeholder: str = ""
    disabled: bool = False
    required: bool = False
    about: str = ""
