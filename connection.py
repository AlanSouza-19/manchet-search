import sqlite3

connection = sqlite3.connect('database.sqlite')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS manchets (title text, link text)''')

connection.commit()

connection.close()
