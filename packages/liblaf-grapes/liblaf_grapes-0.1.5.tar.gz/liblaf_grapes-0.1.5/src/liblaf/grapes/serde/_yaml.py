import io
import os
import warnings
from pathlib import Path
from typing import Any

from liblaf import grapes

from . import AbstractSerializer

with grapes.optional_imports(extra="serde"):
    from ruamel.yaml import YAML


class YAMLSerializer(AbstractSerializer):
    def load(self, fpath: str | os.PathLike[str], **kwargs) -> Any:
        fpath: Path = grapes.as_path(fpath)
        yaml = YAML(**kwargs)
        with fpath.open() as fp:
            return yaml.load(fp)

    def loads(self, data: str, **kwargs) -> Any:
        stream = io.StringIO(data)
        yaml = YAML(**kwargs)
        return yaml.load(stream)

    def dump(self, fpath: str | os.PathLike[str], data: Any, **kwargs) -> None:
        fpath: Path = grapes.as_path(fpath)
        yaml = YAML(**kwargs)
        with fpath.open("w") as fp:
            yaml.dump(data, fp)

    def dumps(self, data: Any, **kwargs) -> str:
        stream = io.StringIO()
        yaml = YAML(**kwargs)
        yaml.dump(data, stream)
        return stream.getvalue()


yaml = YAMLSerializer()
load_yaml = yaml.load
loads_yaml = yaml.loads
dump_yaml = yaml.dump
dumps_yaml = yaml.dumps


@warnings.deprecated("Use `dump_yaml()` instead of `save_yaml()`")
def save_yaml(fpath: str | os.PathLike[str], data: Any) -> None:
    fpath: Path = Path(fpath)
    yaml = YAML()
    with fpath.open("w") as fp:
        yaml.dump(data, fp)
