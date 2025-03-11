from syrius.commands.LoopInputCommand import loopType
from syrius.commands.abstract import AbstractCommand, Command


class ElevenlabsSoundEffectsCommand(Command):
    id: int = 87
    text: str | AbstractCommand | loopType
    api_key: str | AbstractCommand | loopType