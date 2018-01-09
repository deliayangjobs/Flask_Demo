import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text, firstname text, lastname text, email text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

#playlists table
create_table = "CREATE TABLE IF NOT EXISTS playlists (id INTEGER PRIMARY KEY, name text, description text)"
cursor.execute(create_table)
default_value = "INSERT INTO playlists VALUES (Null, 'My Favorate', 'This is a default playlist with my favorite TV and movies.')"
cursor.execute(default_value)
# cursor.execute("INSERT INTO items VALUES (Null, 'test', 10.99)")

#sources table
create_table = "CREATE TABLE IF NOT EXISTS sources (id INTEGER PRIMARY KEY, name text, url text)"
cursor.execute(create_table)
default_value = "INSERT INTO sources VALUES (Null, 'Netflix', 'http://www.netflix.com')"
cursor.execute(default_value)

#tracks table
create_table = "CREATE TABLE IF NOT EXISTS tracks ( \
    id INTEGER PRIMARY KEY, \
    name text, season int, episode int, status text, link text, pix text, \
    playlist INTEGER, source INTEGER, user_id INTEGER, FOREIGN KEY(playlist) REFERENCES playlists(id), \
    FOREIGN KEY(source) REFERENCES sources(id), FOREIGN KEY(user_id) REFERENCES users(id))"
cursor.execute(create_table)

conn.commit()
conn.close()
