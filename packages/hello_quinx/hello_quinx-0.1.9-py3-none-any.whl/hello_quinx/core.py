"""hello_quinx package."""

__version__ = "0.1.9"


class Person:
    def __init__(self, name: str):
        self.name = name


def goodbye() -> str:
    return "Good bye! See you later."
