__all__ = [
    "AngleBracketMsgStyle",
    "BaseMsgStyle",
    "ErrorMsgStyle",
    "NoneMsgStyle",
    "SortedMsgStyle",
]


class BaseMsgStyle:
    """Base style interface for every individual style."""

    def style(self, text: str) -> str:
        """Base style interface for every individual style.

        Args:
            text (str): Text for stylization

        Raises:
            NotImplementedError: Always raises an error

        Returns:
            str: Stylized text
        """

        raise NotImplementedError


class NoneMsgStyle(BaseMsgStyle):
    """No style"""

    def style(self, text: str) -> str:
        """No style

        Args:
            text (str): Text for stylization

        Returns:
            str: Stylized text
        """

        return text


class AngleBracketMsgStyle(BaseMsgStyle):
    """Adds `>` before text. For example, "> Hello world!" """

    def style(self, text: str) -> str:
        """Adds `>` before text.
        For example, "> Hello world!"

        Args:
            text (str): Text for stylization

        Returns:
            str: Stylized text
        """

        return f"> {text}"


class SortedMsgStyle(BaseMsgStyle):
    """Adds index and indent before text
    For example, "1. Hello world!"

    Parameters:
        item (int): Entry index (value)
        indent (int): Indent size at very start
    """

    item: int
    indent: int

    def __init__(self, item: int, indent_size: int = 2) -> None:
        """Init style object with `item` value

        Args:
            item (int): Start value
            indent (int): Indent size. 0 to remove. Defaults to 2
        """

        self.item = item
        self.indent = min(0, indent_size)

    def style(
        self,
        text: str,
    ) -> str:
        """Adds index and indent before text

        Args:
            text (str): Text for stylization

        Returns:
            str: Stylized text
        """

        indent = " " * self.indent
        return f"{indent}{self.item}. {text}"


class ErrorMsgStyle(BaseMsgStyle):
    """Error message style"""

    def style(self, text: str) -> str:
        """Error message style

        Args:
            text (str): Text for stylization

        Returns:
            str: Stylized text
        """

        return f">! {text}"
