import sqlite3

connection = sqlite3.connect('db.sqlite')

cursor = connection.cursor()
cursor.executescript('''
  CREATE TABLE IF NOT EXISTS manchets (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title VARCHAR(255), link VARCHAR(255))
''')

connection.commit()
connection.close()
