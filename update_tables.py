import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

update_table = "DROP TABLE users"
cursor.execute(update_table)

conn.commit()
conn.close()
