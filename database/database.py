import sqlite3
import pathlib
from models import Code, Game


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
        sql = ''' INSERT INTO game(player_name, double_colors, amount_of_colors, amount_of_positions, created_at, code)
                      VALUES(?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, (game.player_name, game.double_colors, game.amount_of_colors, game.amount_of_positions,
                          game.created_at, game.code.colors))
        self.conn.commit()
        return cur.lastrowid

    def get_game(self, id):
        """ Get game object from game table
                specified by the id
            :param id:
            :return: game object
            """
        sql = '''SELECT * FROM game WHERE id=?'''
        cur = self.conn.cursor()
        cur.execute(sql, (id,))

        result = cur.fetchone()
        if result:
            return Game(player_name=result['player_name'], double_colors=result['double_colors'],
                        amount_of_colors=result['amount_of_colors'], amount_of_positions=result['amount_of_positions'],
                        created_at=result['created_at'], completed_at=result['completed_at'],
                        code=Code(result['code']), _id=id)

        return None

    def close_connection(self):
        """ Close the connection to the SQLite database
            """
        self.conn.close()
