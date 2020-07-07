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
    self.connection = sqlite3.connect('db.sqlite')
    self.cursor = self.connection.cursor()

    self.titles = titles
    self.links = links

    self.machets_on_db = self.cursor.execute("SELECT title FROM manchets")
    self.list_of_manchets_on_db: list = []

    for i in self.machets_on_db:
      self.list_of_manchets_on_db.append(i[0])


    for self.title, self.link in zip(self.titles, self.links):
      self.title = self.title.replace("'", "")
      
      if self.title not in self.list_of_manchets_on_db:
        self.cursor.execute(f"INSERT INTO manchets (title, link) VALUES ('{self.title}', '{self.link}')")
      
    self.connection.commit()
    self.connection.close()
