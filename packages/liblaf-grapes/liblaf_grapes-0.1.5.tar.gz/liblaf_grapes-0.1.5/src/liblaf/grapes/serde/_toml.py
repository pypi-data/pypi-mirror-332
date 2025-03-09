import os
import warnings
from pathlib import Path
from typing import Any, override

from liblaf import grapes

from . import AbstractSerializer

with grapes.optional_imports(extra="toml"):
    import tomlkit


class TOMLSerializer(AbstractSerializer):
    @override
    def load(self, fpath: str | os.PathLike[str], **kwargs) -> tomlkit.TOMLDocument:
        fpath: Path = grapes.as_path(fpath)
        with fpath.open() as fp:
            return tomlkit.load(fp, **kwargs)

    @override
    def loads(self, data: str, **kwargs) -> tomlkit.TOMLDocument:
        return tomlkit.loads(data, **kwargs)

    @override
    def dump(self, fpath: str | os.PathLike[str], data: Any, **kwargs) -> None:
        fpath: Path = grapes.as_path(fpath)
        with fpath.open("w") as fp:
            tomlkit.dump(data, fp, **kwargs)

    @override
    def dumps(self, data: Any, **kwargs) -> str:
        return tomlkit.dumps(data, **kwargs)


toml = TOMLSerializer()
load_toml = toml.load
loads_toml = toml.loads
dump_toml = toml.dump
dumps_toml = toml.dumps


@warnings.deprecated("Use `dump_toml()` instead of `save_toml()`")
def save_toml(
    fpath: str | os.PathLike[str], data: Any, *, sort_keys: bool = False
) -> None:
    """Save data to a TOML file.

    Args:
        fpath: The file path where the TOML data will be saved.
        data: The data to be serialized and saved in TOML format.
        sort_keys: Whether to sort the keys in the output.
    """
    fpath: Path = Path(fpath)
    with fpath.open("w") as fp:
        tomlkit.dump(data, fp, sort_keys=sort_keys)
