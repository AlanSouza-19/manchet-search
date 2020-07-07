import sqlite3

def add(a:list, b: list):
  connection = sqlite3.connect('db.sqlite')
  cursor = connection.cursor()
  z = zip(a, b)

  for title, link in z:
    title = title.replace("'", "")
    cursor.execute(f"INSERT INTO manchets (title, link) VALUES ('{title}', '{link}')")
  
  connection.commit()
  connection.close()