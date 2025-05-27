from enum import Enum, auto

class GameState(Enum):
    Start = auto()
    Loading = auto()
    Quiz = auto()
    ExitConfirm = auto()
    Sad = auto()
