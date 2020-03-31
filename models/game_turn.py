import datetime as dt
import random


class GameTurn:
    def __init__(self, game_id, code_guessed, _id=None, submitted_at=None):
        self.game_id = game_id
        self.code_guessed = code_guessed
        self.id = _id
        self.submitted_at = submitted_at if submitted_at else dt.datetime.now()

    def get_feedback_pins(self, correct_code):
        pins = []

        for guessPos in range(len(self.code_guessed)):
            guess = self.code_guessed[guessPos]

            for codePos in range(len(correct_code)):
                color = correct_code[codePos]

                # Guess correct color and same position
                if guessPos == codePos and guess == color:
                    pins.append("black")
                    break

                # Guess correct color but wrong position
                elif guess == color:
                    pins.append("white")
                    break

        # Shuffle feedback pins so that the player can't make any guesses
        random.shuffle(pins)
        return pins
