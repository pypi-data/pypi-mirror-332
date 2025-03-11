from collections.abc import Sequence

import loguru

from . import Filter

DEFAULT_FILTER: Filter = {
    "": "INFO",
    "__main__": "TRACE",
    "liblaf": "DEBUG",
}


DEFAULT_LEVELS: Sequence["loguru.LevelConfig"] = [
    {"name": "ICECREAM", "no": 15, "color": "<magenta><bold>", "icon": "🍦"}
]
