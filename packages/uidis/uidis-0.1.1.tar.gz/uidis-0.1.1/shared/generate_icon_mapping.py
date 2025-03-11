from itertools import chain, starmap
from requests import get
from pathlib import Path
from msgspec import Struct
from msgspec.json import decode, encode as encode_json
from msgspec.msgpack import encode as encode_pack

repo = Path(__file__).parent.parent
backend_map = repo / "uidis" / "assets" / "maps" / "icons.pack"
frontend_map = repo / "web" / "maps" / "icons.json"

print("Generating Icon Mapping...")
print("Repository:\n -", repo)
print("Backend Icon Map:\n -", backend_map)
print("Frontend Icon Map:\n -", frontend_map)

# first 5 characters are `)]}'`, then JSON
data = get("https://fonts.google.com/metadata/icons?key=material_symbols&incomplete=true").text[5:]


class _Icon(Struct):
    popularity: int
    name: str
    unsupported_families: tuple[str, ...]

    def is_supported(self) -> bool:
        return not any("Symbol" in family for family in self.unsupported_families)


class _IconRepo(Struct):
    icons: tuple[_Icon, ...]


icons = decode(data, type=_IconRepo).icons
supported_icons = filter(_Icon.is_supported, icons)
popularity_sorted = (i.name for i in sorted(supported_icons, key=lambda i: i.popularity, reverse=True))
size_optimised_ids = chain.from_iterable(
    starmap(
        range,
        (
            (-(1 << 5), (1 << 7)),  # integers ranging from 5-bit negative to 7-bit positive are encoded as one byte
            (-(1 << 7), -(1 << 5)),  # 7-bit negative -> 2 bytes
            ((1 << 7), (1 << 16)),  # 8-bit positive -> 2 bytes; 16-bit positive -> 3 bytes
            (-(1 << 15), -(1 << 7)),  # 16-bit negative -> 3 bytes
        ),
    )
)

icon_id_to_name = tuple(zip(size_optimised_ids, popularity_sorted))

with frontend_map.open("wb") as f:
    f.write(encode_json(icon_id_to_name))

with backend_map.open("wb") as f:
    f.write(encode_pack({v: k for k, v in icon_id_to_name}))
