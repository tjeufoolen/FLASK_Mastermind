import datetime as dt


class GameTurn:
    def __init__(self, game_id, code_guessed, _id=None, submitted_at=None):
        self.game_id = game_id
        self.code_guessed = code_guessed
        self.id = _id
        self.submitted_at = submitted_at if submitted_at else dt.datetime.now()
