from typing import Any

__all__ = ["Location"]


class Location:
    _name: str
    _actions = dict

    def __init__(self, name: str, actions: dict[Any, Any]) -> None:
        # TODO: change dict[Any, Any] to a specific type

        self._name = name
        self._actions = actions

    def enter(self) -> None:
        pass

    def update(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def __repr__(self) -> str:
        return self._name.strip().capitalize()
