import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

#track table
create_table = "CREATE TABLE IF NOT EXISTS tracks (id INTEGER PRIMARY KEY, playlist int, source int, name text, season int, episode int, status text, link text, pix text)"
cursor.execute(create_table)

# cursor.execute("INSERT INTO items VALUES (Null, 'test', 10.99)")

conn.commit()
conn.close()
