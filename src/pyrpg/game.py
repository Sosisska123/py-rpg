import time
from collections.abc import Callable
from pathlib import Path
from typing import ParamSpec, TypeVar

from .action import Action
from .components.msg_style import *
from .location import Location
from .player import Player
from .printer import Printer

P = ParamSpec("P")
R = TypeVar("R")

__all__ = ["Game"]


class Game:
    DEFAULT_SAVE_PATH = Path.home() / "rpgmaker" / "123"

    def __init__(
        self,
        player: Player,
        message_style: BaseMsgStyle | None,
        save_path: Path | str = DEFAULT_SAVE_PATH,
        auto_capitalize: bool = False,
        timeout: int = 0,
    ) -> None:
        self.timeout = timeout
        self._is_playing = False
        self._player = player
        self._save_path = Path(save_path)
        self.printer = Printer(
            default_msg_style=message_style,
            auto_capitalize=auto_capitalize,
        )

    def start(
        self,
        game_func: Callable[P, R],
        message: str = "",
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> None:
        """Starts the game and prints welcome message"""

        if message.strip():
            self.print(message)

        try:
            self._is_playing = True
            game_func(*args, **kwargs)
        except KeyboardInterrupt:
            self.printer.print(
                "\nИгра прервана. Завершение...",
                ErrorMsgStyle(),
            )
        finally:
            self.end()

    def is_playing(self) -> bool:
        """Returns the state of the game"""

        return self._is_playing

    def end(self):
        self._is_playing = False

    def get_current_location(self) -> Location:
        """Get current `Location` of the player"""

        return self._player.current_location()

    def choice(
        self,
        message: str,
        actions: list[Action],
        show_variants: bool = False,
    ) -> Action:
        """Ask for the player action from the given `Action's`.
        Basicly its the `input()` with answer matching and infininte asking loop.
        Supports selecting by index

        Parameters:
            message: Text to print before the input. Equivalent to `input(message)`
            actions: List of available actions
            show_variants: Print each `Action` name with its sequence number

        Returns:
            Action: Selected `Action`
        """

        action_names = [variant.name.lower() for variant in actions]
        action_names_str = f" ({', '.join(action_names)})"
        self.print(f"{message}{action_names_str if len(actions) > 0 else ''}:")

        if show_variants:
            sl_style = SortedMsgStyle(0)
            for i, action in enumerate(actions):
                sl_style.item = i + 1
                self.printer.print(action.name, sl_style)

        while True:
            usr_input = input(">> ")
            usr_input = usr_input.strip().lower()

            # TODO: fuzzy matching
            for ac in actions:
                if usr_input == ac.name.lower():
                    return ac

            try:
                idx = int(usr_input)
                if not 0 < idx <= len(actions):
                    raise IndexError()
                return actions[idx - 1]
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
        """Prints the provided text with default style"""

        time.sleep(self.timeout)
        self.printer.print(text=text)

    def set_timeout(self, secs: int):
        """Set timeout before print message. Works only when single-threaded"""

        self.timeout = secs
