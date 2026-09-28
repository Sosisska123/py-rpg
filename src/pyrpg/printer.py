from .components.msg_style import *

__all__ = ["Printer"]


class Printer:
    def __init__(
        self,
        default_msg_style: BaseMsgStyle | None,
        auto_capitalize: bool = False,
    ) -> None:
        self._msg_style = default_msg_style or NoneMsgStyle()
        self._auto_capitalize = auto_capitalize

    def print(self, text: str, custom_style: BaseMsgStyle | None = None) -> None:
        """Prints provided text with defined style"""

        self._print(text=text, custom_style=custom_style)

    def _print(self, text: str, custom_style: BaseMsgStyle | None = None) -> None:
        """Internal print impl. Applies all styles to the given text and prints it"""

        text = text.strip()
        if not text:
            return

        line_style = custom_style or self._msg_style
        text = "".join([text[0].upper(), text[1:]]) if self._auto_capitalize else text
        text = line_style.style(text)

        print(text)
