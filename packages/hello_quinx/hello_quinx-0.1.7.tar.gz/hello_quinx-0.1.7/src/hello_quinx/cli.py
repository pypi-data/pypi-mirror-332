from ._version import __version__

class Console:
    def __init__(self):
        self.commands = ['list', 'help']

    def add_command(self, command: str) -> Console:
        self.commands.append(command)
        return self

    def run(self):
        print(f'hello_quinx CLI {__version__}')

        print(self.commands)


app = Console()

if __name__ == "__main__":
    app.run()
