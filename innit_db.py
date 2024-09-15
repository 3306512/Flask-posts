import sqlite3


connection = sqlite3.connect("database.db")
with open("schema.sql") as schema:
    connection.executescript(schema.read())

cursor = connection.cursor()
cursor.execute("""
    INSERT INTO posts (title, content)
    VALUES (?, ?)
""", ("Test post 1", "content for test post 1"))
cursor.execute("""
    INSERT INTO posts (title, content)
    VALUES (?, ?)
""", ("Test post 2", "content for test post 2"))
connection.commit()
connection.close()
