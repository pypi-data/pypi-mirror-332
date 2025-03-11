from __future__ import annotations
from pathlib import Path
from typing import overload

from msgspec.msgpack import decode
from msgspec import Struct

from .shared import DIR_LOOKUPS

Lookups: dict[str, Lookup] = {}


class Lookup(Struct):
    code_to_name: dict[int, str]
    name_to_code: dict[str, int]

    def __setitem__(self, key: str, value: int):
        self.code_to_name[value] = key
        self.name_to_code[key] = value

    @overload
    def __getitem__(self, key: str) -> int: ...

    @overload
    def __getitem__(self, key: int) -> str: ...

    def __getitem__(self, key: str | int) -> int | str:
        return self.code_to_name[key] if isinstance(key, int) else self.name_to_code[key]

    @classmethod
    def new(cls, name: str, path: Path | None = None) -> Lookup:
        if name in Lookups:
            raise ValueError(f"Lookup {name!r} already exists")
        name_to_code = decode(path.read_bytes(), type=dict[str, int]) if path else {}
        lookup = cls({v: k for k, v in name_to_code.items()}, name_to_code)
        Lookups[name] = lookup
        return lookup


for path in DIR_LOOKUPS.iterdir():
    Lookup.new(path.stem, path)
