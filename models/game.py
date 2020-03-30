import datetime as dt
from .code import Code
import random


class Game:
    __colors = ['red', 'orange', 'yellow', 'mintgreen', 'green', 'aqua', 'cyan', 'pink', 'purple', 'brown']

    def __init__(self, player_name, double_colors, amount_of_colors, amount_of_positions,
                 created_at=None, completed_at=None, code=None, _id=None):
        # Set instance variables
        self.player_name = player_name
        self.double_colors = double_colors
        self.amount_of_colors = amount_of_colors
        self.amount_of_positions = amount_of_positions

        # Set optional variables
        self.created_at = created_at if created_at else dt.datetime.now()
        self.completed_at = completed_at if completed_at else None
        self.code = code if code else self.__generate_code()
        self.id = _id if _id else self.__generate_code()

    def __generate_code(self):
        """ Generate a code object with an array of colors
            :return: Code object
            """
        colors = self.__colors[0:self.amount_of_colors]
        code_colors = ""

        for pos in range(self.amount_of_positions):
            color = random.choice(colors)
            if not self.double_colors:
                colors.remove(color)
            if not pos == 0:
                code_colors += ", "
            code_colors += color

        return Code(code_colors)
