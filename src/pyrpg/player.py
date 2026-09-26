from typing import Any

from .components import Bank, Health
from .location import Location

__all__ = ["Player"]


class Player:
    _name: str
    _health: Health
    _money: Bank
    _location: Location

    def __init__(
        self,
        name: str,
        location: Location,
        health: Health | Any | None = None,
        money: Bank | Any | None = None,
    ) -> None:
        h = Health()
        b = Bank()

        self._name = name
        self._location = location
        self._health = h
        self._money = b

    @property
    def name(self) -> str:
        return self._name
