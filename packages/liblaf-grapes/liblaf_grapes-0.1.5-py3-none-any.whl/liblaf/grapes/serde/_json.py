import json as json_
import os
import warnings
from pathlib import Path
from typing import Any, override

from liblaf import grapes

from . import AbstractSerializer


class JSONSerializer(AbstractSerializer):
    @override
    def load(self, fpath: str | os.PathLike[str], **kwargs) -> Any:
        fpath: Path = grapes.as_path(fpath)
        with fpath.open() as fp:
            return json_.load(fp, **kwargs)

    @override
    def loads(self, data: str, **kwargs) -> Any:
        return json_.loads(data, **kwargs)

    @override
    def dump(self, fpath: str | os.PathLike[str], data: Any, **kwargs) -> None:
        fpath: Path = grapes.as_path(fpath)
        with fpath.open("w") as fp:
            json_.dump(data, fp, **kwargs)

    @override
    def dumps(self, data: Any, **kwargs) -> str:
        return json_.dumps(data, **kwargs)


json = JSONSerializer()
load_json = json.load
loads_json = json.loads
dump_json = json.dump
dumps_json = json.dumps


@warnings.deprecated("Use `dump_json()` instead of `save_json()`")
def save_json(fpath: str | os.PathLike[str], data: Any) -> None:
    """Save data to a JSON file.

    Args:
        fpath: The file path where the JSON data will be saved.
        data: The data to be serialized to JSON and saved to the file.
    """
    fpath: Path = Path(fpath)
    with fpath.open("w") as fp:
        json.dump(data, fp)
