from pathlib import Path

from .components.msg_style import MsgStyle
from .player import Player

DEFAULT_SAVE_PATH = Path.joinpath(Path.home(), "rpgmaker", "123")

__all__ = ["Game"]


class Game:
    _is_playing: bool
    _msg_style: MsgStyle
    _player: Player

    _save_path: Path = DEFAULT_SAVE_PATH

    def __init__(
        self,
        player: Player,
        message_style: MsgStyle | None = None,
        save_path: Path | str | None = None,
    ) -> None:
        self._player = player

        if message_style is not None:
            self._msg_style = message_style

        if save_path is not None:
            self._save_path = Path(save_path)

    def start(self, message: str | None = None):
        if message is not None:
            self._print(message)

        self._is_playing = True

    def is_playing(self) -> bool:
        return self._is_playing

    def _print(self, text: str):
        pass
