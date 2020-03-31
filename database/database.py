import sqlite3
import pathlib
import json
from models import Game, Player, GameTurn


def create_connection(db_file):
    """ Create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
    conn = None
    try:
        file = str(pathlib.Path().absolute()) + "/storage/" + db_file
        conn = sqlite3.connect(file, check_same_thread=False)
        conn.row_factory = sqlite3.Row
    except sqlite3.Error as e:
        print(e)

    return conn


class Database:
    def __init__(self, db_file):
        self.conn = create_connection(db_file)

    def create_game(self, game):
        """ Create a new game into the game table
            :param game:
            :return: game id
            """
        sql = ''' INSERT INTO game(player_name, double_colors, amount_of_colors, amount_of_positions, created_at, code, 
                  color_options) VALUES(?,?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, (game.player.name, game.double_colors, game.amount_of_colors, game.amount_of_positions,
                          game.created_at, json.dumps(game.code), json.dumps(game.color_options)))
        self.conn.commit()
        return cur.lastrowid

    def get_game(self, id):
        """ Get game object from game table
                specified by the id
            :param id:
            :return: game object
            """
        cur = self.conn.cursor()
        cur.execute('''SELECT * FROM game WHERE id=?''', (id,))
        game = cur.fetchone()

        if game:
            turns = self.get_game_turns(id)
            g = Game(player=Player(game['player_name']), double_colors=game['double_colors'],
                     amount_of_colors=game['amount_of_colors'], amount_of_positions=game['amount_of_positions'],
                     color_options=json.loads(game['color_options']), created_at=game['created_at'],
                     completed_at=game['completed_at'], code=json.loads(game['code']), _id=id, turns=turns)
            return g
        return None

    def get_game_turns(self, game_id):
        """ Get game turns from games turn table
                specified by the game id
            :param game_id:
            :return: Array of game turn objects
            """
        cur = self.conn.cursor()
        cur.execute('''SELECT * FROM game_turn WHERE game_id = ?''', (game_id,))
        rows = cur.fetchall()

        turns = []
        for row in rows:
            turns.append(GameTurn(game_id=["game_id"], _id=row["id"], submitted_at=row["submitted_at"],
                                  code_guessed=json.loads(row["code_guessed"])))

        return turns

    def create_game_turn(self, turn):
        sql = '''INSERT INTO game_turn (game_id, submitted_at, code_guessed) VALUES (?,?,?)'''
        cur = self.conn.cursor()
        cur.execute(sql, (turn.game_id, turn.submitted_at, json.dumps(turn.code_guessed)))
        self.conn.commit()

    def close_connection(self):
        """ Close the connection to the SQLite database
            """
        self.conn.close()
