import sqlite3

class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name':self.name, 'price':self.price}

    def insert(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "INSERT INTO items VALUES (Null, ?, ?)"
        cursor.execute(query, (self.name, self.price))

        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (self.price, self.name))

        conn.commit()
        conn.close()

    @classmethod
    def find_by_name(cls, name):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        conn.close()

        if row:
            return cls(row[1], row[2])
