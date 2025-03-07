from .core import __version__


class Console:
    def __init__(self):
        self.commands = ["list", "help"]

    def add_command(self, command: str):
        self.commands.append(command)
        return self

    def run(self):
        print(f"hello_quinx CLI {__version__}")

        print("\nAvailable commands:")

        for command in self.commands:
            print(f"  {command}")


def app():
    console = Console()
    console.run()


if __name__ == "__main__":
    app()
