from dataclasses import dataclass
from typing import Any

__all__ = ["Action"]


@dataclass(frozen=True)
class Action:
    name: str
    code: Any
