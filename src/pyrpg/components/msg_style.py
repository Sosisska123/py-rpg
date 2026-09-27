__all__ = [
    "AngleBracketMsgStyle",
    "BaseMsgStyle",
    "ErrorMsgStyle",
    "NoneMsgStyle",
    "SortedMsgStyle",
]


class BaseMsgStyle:
    def style(self, text: str) -> str:
        raise NotImplementedError


class NoneMsgStyle(BaseMsgStyle):
    def style(self, text: str) -> str:
        return text


class AngleBracketMsgStyle(BaseMsgStyle):
    def style(self, text: str) -> str:
        return f"> {text}"


class SortedMsgStyle(BaseMsgStyle):
    item: int

    def __init__(self, item: int) -> None:
        self.item = item

    def style(
        self,
        text: str,
    ) -> str:
        return f"  {self.item}. {text}"


class ErrorMsgStyle(BaseMsgStyle):
    def style(self, text: str) -> str:
        return f">! {text}"
