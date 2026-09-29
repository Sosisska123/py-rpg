from dataclasses import dataclass

__all__ = ["Health"]


@dataclass
class Health:
    value: int | float
