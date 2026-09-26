from argparse import Action
from dataclasses import dataclass

__all__ = ["Location"]


@dataclass(frozen=True)
class Location:
    name: str
    actions: list[Action]

    def add_action(self, action: Action) -> None:
        self.actions.append(action)
