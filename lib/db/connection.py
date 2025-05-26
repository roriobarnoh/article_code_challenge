import sqlite3


db_connection = sqlite3.connect('my_database.db')
db_cursor = db_connection.cursor()
