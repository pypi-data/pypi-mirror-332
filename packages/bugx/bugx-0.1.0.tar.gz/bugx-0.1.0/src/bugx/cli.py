""" CLI """

from typing import NoReturn, Self

from typer import Exit, Typer, echo, run

from bugx.cli_constants import CliApplication


class TyperCommand:
    """Typer Command"""

    EPILOG = CliApplication.EPILOG

    def __init__(self, app: Typer, name: str):
        self.app = app
        self.option_name = name

    def add(self) -> Self:
        self.app.command(epilog=self.EPILOG)(self.option_name)
        return self


def cli_exit() -> NoReturn:
    raise Exit(code=1)


def main():
    print("Hello from bux!")
    TyperCommand(app=Typer(), name="cli_exit").add()


if __name__ == "__main__":
    run(function=main)
