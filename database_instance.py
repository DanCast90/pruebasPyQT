import sqlite3
import os

class database_conection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'data', 'prueba.db')
    conn=sqlite3.connect(db_path)
    cursor=""
    def connect(self):
        cursor=self.conn.cursor()
        return cursor

    def desconnect(self):
        self.conn.close()