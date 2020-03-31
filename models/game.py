import datetime as dt
import random


class Game:
    __colors = ['red', 'orange', 'yellow', 'mintgreen', 'green', 'aqua', 'cyan', 'pink', 'purple', 'brown']

    def __init__(self, player, double_colors, amount_of_colors, amount_of_positions,
                 color_options=None, created_at=None, completed_at=None, code=None, _id=None, turns=None):
        # Set instance variables
        self.player = player
        self.double_colors = double_colors
        self.amount_of_colors = amount_of_colors
        self.amount_of_positions = amount_of_positions

        # Set color options
        self.color_options = color_options if color_options else self.__colors[0:self.amount_of_colors]

        # Set optional variables
        self.created_at = created_at if created_at else dt.datetime.now()
        self.completed_at = completed_at
        self.code = code if code else self.__generate_code()
        self.id = _id
        self.turns = turns

    def __generate_code(self):
        """ Generate a code object with an array of colors
            :return: Array of colors
            """
        colors = self.color_options.copy()
        code_colors = []

        for pos in range(self.amount_of_positions):
            color = random.choice(colors)
            if not self.double_colors:
                colors.remove(color)
            code_colors.append(color)

        return code_colors
