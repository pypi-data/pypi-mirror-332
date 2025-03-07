"""hello_quinx package."""

__version__ = "0.2.0"


class Person:
    def __init__(self, name: str):
        self.name = name


def goodbye() -> str:
    return "Good bye! See you later."
