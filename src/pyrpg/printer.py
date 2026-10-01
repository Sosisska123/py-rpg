from .components.msg_style import *

__all__ = ["Printer"]


class Printer:
    def __init__(
        self,
        default_msg_style: BaseMsgStyle | None,
        auto_capitalize: bool = False,
    ) -> None:
        """Creates the `Printer`

        Args:
            default_msg_style (BaseMsgStyle | None): Style of all printed messages. Defaults to None Style.
            auto_capitalize (bool, optional): Makes all the provided strings capital. Defaults to False.
        """

        self._msg_style = default_msg_style or NoneMsgStyle()
        self._auto_capitalize = auto_capitalize

    def print(self, text: str, custom_style: BaseMsgStyle | None = None) -> None:
        """Prints provided text with defined style

        Args:
            text (str): Text to print
            custom_style (BaseMsgStyle | None, optional): Custom message style. If None uses default. Defaults to None.
        """

        self._print(text=text, custom_style=custom_style)

    def print_error(self, text: str):
        """Shortcut for printing errors

        Args:
            text (str): Text to print
        """

        self._print(text=text, custom_style=ErrorMsgStyle())

    def _print(self, text: str, custom_style: BaseMsgStyle | None = None) -> None:
        """Internal print impl. Applies all styles to the given text and prints it"""

        text = text.strip()
        if not text:
            return

        line_style = custom_style or self._msg_style
        text = "".join([text[0].upper(), text[1:]]) if self._auto_capitalize else text
        text = line_style.style(text)

        print(text)
