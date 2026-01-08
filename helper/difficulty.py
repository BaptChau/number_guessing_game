from enum import Enum

class Difficulty(Enum):
    EASY=10
    MEDIUM=5
    HARD=3

    @staticmethod
    def get_dificulty_from_value(value: int):
        if value == 1:
            return Difficulty.EASY
        elif value == 2:
            return Difficulty.MEDIUM
        elif value == 3:
            return Difficulty.HARD
        return None