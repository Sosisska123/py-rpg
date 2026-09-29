from dataclasses import dataclass

__all__ = ["Bank"]


@dataclass(repr=False)
class Bank:
    value: int | float
    currency: str

    def __repr__(self) -> str:
        return f"{str(self.value).capitalize()} {self.currency}"
