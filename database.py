import sqlite3

class Connection:
  def __init__(self):
    self.connection = sqlite3.connect('db.sqlite')
    self.cursor = self.connection.cursor()
    self.cursor.executescript('''
      CREATE TABLE IF NOT EXISTS manchets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255),
        link VARCHAR(255))''')

    self.connection.commit()
    self.connection.close()

  def add(self, titles: list, links: list):
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()

    for title, link in zip(titles, links):
      title = title.replace("'", "")
      cursor.execute(f"INSERT INTO manchets (title, link) VALUES ('{title}', '{link}')")
  
    connection.commit()
    connection.close()
