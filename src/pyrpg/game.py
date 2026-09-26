from pathlib import Path

from .components.msg_style import MsgStyle
from .player import Player

__all__ = ["Game"]


class Game:
    DEFAULT_SAVE_PATH = Path.joinpath(Path.home(), "rpgmaker", "123")

    _is_playing: bool
    _msg_style: MsgStyle
    _player: Player

    _save_path: Path = DEFAULT_SAVE_PATH

    _auto_capitalize: bool

    def __init__(
        self,
        player: Player,
        message_style: MsgStyle = MsgStyle.NONE,
        save_path: Path | str = DEFAULT_SAVE_PATH,
        auto_capitalize: bool = False,
    ) -> None:
        self._player = player
        self._msg_style = message_style
        self._save_path = Path(save_path)
        self._auto_capitalize = auto_capitalize

    def start(self, message: str = "") -> None:
        """Starts the game and prints welcome message"""

        if not message.strip():
            self._print(message, None)

        self._is_playing = True

    def is_playing(self) -> bool:
        """Returns the state of the game"""

        return self._is_playing

    def print(self, text: str) -> None:
        """Prints provided text with defined style"""

        self._print(text=text, custom_style=None)

    def _print(self, text: str, custom_style: MsgStyle | None = None) -> None:
        """Internal print impl. Applies all styles to the given text and prints it"""

        line_style = custom_style or self._msg_style
        match line_style:
            case MsgStyle.NONE:
                prefix = ""
            case MsgStyle.ANGLE_BRACKET:
                prefix = ">"

        text = text.capitalize() if self._auto_capitalize else text

        line = f"{prefix} {text}"
        print(line)
