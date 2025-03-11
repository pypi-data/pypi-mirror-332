from itertools import chain, starmap
from os import environ
from pathlib import Path
from typing import Any
from importlib.metadata import version as package_version

from fastapi.responses import Response
from msgspec.msgpack import Encoder

encode = Encoder().encode

IS_DEV = environ.get("DEV", False)

DIR_ROOT: Path = Path(__file__).parent
DIR_ASSETS: Path = DIR_ROOT / "assets"
DIR_LOOKUPS: Path = DIR_ASSETS / "lookups"

HEADERS = {"Access-Control-Allow-Origin": "*"} if IS_DEV else {}
__version__ = (0, 0, 0) if IS_DEV else tuple(map(int, package_version("uidis").split("+")[0].split(".")))


def escape(s: str) -> str:
    return (
        s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")
    )


def pack(struct: Any) -> Response:
    return Response(encode(struct), media_type="uidis", headers=HEADERS)


def iter_size_optimised_ids() -> chain[int]:
    return chain.from_iterable(
        starmap(
            range,
            (
                (-(1 << 5), (1 << 7)),  # integers ranging from 5-bit negative to 7-bit positive are encoded as one byte
                (-(1 << 7), -(1 << 5)),  # 7-bit negative --> 2 bytes
                ((1 << 7), (1 << 16)),  # 8-bit positive --> 2 bytes; 16-bit positive --> 3 bytes
                (-(1 << 15), -(1 << 7)),  # 16-bit negative --> 3 bytes
            ),
        )
    )
