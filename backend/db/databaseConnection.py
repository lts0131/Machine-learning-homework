"""
@File    : databaseConnection.py
@Date    : 2023-03-05
@Author  : LiuTianSheng
@Software : backend
"""
import sqlite3


class DatabaseConnection:

    def __init__(self):
        self.conn = self.get_db_connection()

    def get_db_connection(self):
        conn = sqlite3.connect('db/database.db')
        conn.row_factory = sqlite3.Row
        return conn
