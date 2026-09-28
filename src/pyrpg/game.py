from pathlib import Path
from typing import Any

from pyrpg.printer import Printer

from .action import Action
from .components.msg_style import *
from .location import Location
from .player import Player

__all__ = ["Game"]


class Game:
    DEFAULT_SAVE_PATH = Path.joinpath(Path.home(), "rpgmaker", "123")

    def __init__(
        self,
        player: Player,
        message_style: BaseMsgStyle | None,
        save_path: Path | str = DEFAULT_SAVE_PATH,
        auto_capitalize: bool = False,
    ) -> None:
        self._is_playing = False
        self._player = player
        self._save_path = Path(save_path)
        self.printer = Printer(
            default_msg_style=message_style,
            auto_capitalize=auto_capitalize,
        )

    def start(self, message: str = "") -> None:
        """Starts the game and prints welcome message"""

        if not message.strip():
            self.print(message)

        self._is_playing = True

    def is_playing(self) -> bool:
        """Returns the state of the game"""

        return self._is_playing

    def get_current_location(self) -> Location:
        """Get current location of the player"""

        return self._player.current_location()

    def choice(
        self,
        message: str,
        actions: list[Action],
        show_variants: bool = False,
    ) -> Any:
        action_names = [variant.name for variant in actions]
        action_names_str = f" ({', '.join(action_names)})" if show_variants else ""
        self.print(f"{message}{action_names_str}:")

        sl_style = SortedMsgStyle(0)
        for i, action in enumerate(actions):
            sl_style.item = i + 1
            self.printer.print(action.name, sl_style)

        while True:
            usr_input = input("> ")
            usr_input = usr_input.strip().lower()

            # TODO: fuzzy matching
            for ac in actions:
                if usr_input == ac.name.lower():
                    return ac.code

            try:
                idx = int(usr_input)
                if idx < 0:
                    raise IndexError(f"Negative index {usr_input}")
                return actions[idx - 1].code
            except ValueError:
                self.printer.print(
                    f"Неверный ввод: варианта «{usr_input}» нет в списке!",
                    ErrorMsgStyle(),
                )
            except IndexError:
                self.printer.print(
                    f"Неверный ввод: числа «{usr_input}» нет в списке!",
                    ErrorMsgStyle(),
                )

    def print(self, text: str):
        """Prints provided text with default style"""

        self.printer.print(text=text)
