import time
from collections.abc import Callable
from pathlib import Path
from typing import ParamSpec, TypeVar

from .action import Action
from .components.msg_style import *
from .location import Location
from .player import Player
from .printer import Printer

__all__ = ["Game"]


class Game:
    P = ParamSpec("P")
    R = TypeVar("R")
    DEFAULT_SAVE_PATH = Path.home() / "rpgmaker" / "123"

    # TODO: add save/load and stop (to not end the game completely).

    def __init__(
        self,
        player: Player | None = None,
        message_style: BaseMsgStyle | None = None,
        save_path: Path | str = DEFAULT_SAVE_PATH,
        auto_capitalize: bool = False,
        timeout: int = 0,
    ) -> None:
        """Initializes a completely new `Game` instance

        Args:
            player (Player | None, optional): Main player. If not provided, starts the new player creation procedure.
            message_style (BaseMsgStyle | None, optional): Style of all messages printed using `self.print()`. Defaults to None Style.
            save_path (Path | str, optional): (Unused) Path of the game saves. Defaults to `home/rpgmaker/123`.
            auto_capitalize (bool, optional): Makes all the provided strings capital. Defaults to False.
            timeout (int, optional): Time between each message, in secs. Defaults to 0.
        """

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
        """Starts the game and prints welcome message

        Args:
            game_func (Callable[P, R]): Main game function. Runs at start, stops when player looses
            message (str, optional): Welcome message. Prints if not empty. Defaults to None.
            *args: Additional args.
            **kwargs: Additional kewword args.
        """

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
        """State of the game"""

        return self._is_playing

    def end(self):
        """Ends the game"""

        self._is_playing = False

    def choice(
        self,
        actions: list[Action],
        message: str = "",
        show_variants: bool = False,
    ) -> Action:
        """Ask for the player action from the given `Action's`.
        Basicly its the `input()` with answer matching and infininte asking loop.
        Supports selecting by index

        Args:
            actions (list[Action]): List of available actions
            message (str, optional): Text to print before the input. Equivalent to `input(message)`. Defaults to None.
            show_variants (bool, optional): Print each `Action` name with its sequence number. Defaults to False.

        Returns:
            Action: One selected `Action`
        """
        # TODO: add allow multipel actions

        if message:
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
                self.printer.print_error(
                    f"Неверный ввод: варианта «{usr_input}» нет в списке!"
                )
            except IndexError:
                self.printer.print_error(
                    f"Неверный ввод: числа «{usr_input}» нет в списке!"
                )

    def print(self, text: str) -> None:
        """Prints the provided text with default style

        Args:
            text (str): Text to print. Not printing anything if `text` is empty
        """

        if not text:
            return

        time.sleep(self.timeout)
        self.printer.print(text=text)

    def set_timeout(self, secs: int) -> None:
        """Set timeout before print message. Works only when single-threaded

        Args:
            secs (int): Seconds between each message. 0 or negative value removes the timeout
        """

        self.timeout = min(0, secs)

    def set_player(self, player: Player) -> None:
        """Assings the new player if its not set at init.
        (unueful because init calls `create_player`)

        Args:
            player (Player): New created player
        """

        if self._player:
            self.printer.print_error("Игрок уже создан")
            return

        self._player = player

    def create_player(self, start_location: Location) -> Player:
        """Creates the player instance in given location

        Args:
            start_location (Location): Start player location

        Returns:
            Player: New player
        """

        self.print("Введите имя игрока")
        usr_input = input(">> ")
        usr_input = usr_input.strip().lower()
        return Player(name=usr_input, location=start_location)
