from dataclasses import dataclass

from .action import Action

__all__ = ["Location"]


@dataclass(frozen=True)
class Location:
    name: str
    actions: list[Action]

    def add_action(self, action: Action) -> None:
        self.actions.append(action)

    def __repr__(self) -> str:
        return self.name.strip().capitalize()
