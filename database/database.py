import sqlite3


class Database:
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
                specified by the db_file
            :param db_file: database file
            :return: Connection object or None
            """
        conn = None
        try:
            conn = sqlite3.connect("./storage/" + db_file)
        except sqlite3.Error as e:
            print(e)

        return conn

    def close_connection(self):
        """ close the connection to the SQLite database
            """
        self.conn.close()
