import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user_info (user_name, password,user_type,user_nickname) VALUES (?,?,?,?)",
            ('lts', '123456', 'admin', 'George Liu'))

connection.commit()
connection.close()
