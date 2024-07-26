# importing sqlite

import sqlite3 as lite

# creating connection

con = lite.connect('data.db')

# creating table

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE inventory(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, place TEXT, description TEXT, brand TEXT, purchase_date DATE, price DECIMAL, series TEXT, image TEXT)")