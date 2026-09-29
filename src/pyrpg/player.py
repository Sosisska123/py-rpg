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
        health: Health | Any = Health,
        money: Bank | Any = Bank,
    ) -> None:
        self._name = name
        self._location = location
        self._health = health
        self._money = money

    def current_location(self) -> Location:
        return self._location

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> str:
        return repr(self._location)

    @property
    def health(self) -> str:
        return repr(self._health)

    @property
    def money(self) -> str:
        return repr(self._money)

    def stats(self) -> dict[str, str]:
        return {
            "Имя": self.name,
            "Локация": self.location,
            "Здоровье": self.health,
            "Деньги": self.money,
        }
