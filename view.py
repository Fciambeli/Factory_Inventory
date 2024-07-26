# importing sqlite

import sqlite3 as lite

# creating connection

con = lite.connect('data.db')

# CRUD - create, reade, update, delete

# create data

def insert_form(i):

    with con:
        cur = con.cursor()
        query = "INSERT INTO inventory(name, place, description, brand, purchase_date, price, series, image) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query, i)

# update data

def update_form(i):

    with con:
        cur = con.cursor()
        query = "UPDATE inventory SET name=?, place=?, description=?, brand=?, purchase_date=?, price=?, series=?, image=? WHERE id=?"
        cur.execute(query, i)

# read data

def read_form():

    read_data = []

    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventory"
        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            read_data.append(row)
    return read_data

# delete data

def delete_form(i):

    with con:
        cur = con.cursor()
        query = "DELETE FROM inventory WHERE id=?"
        cur.execute(query, i)

# read individual data

def read_item(id):

    read_individual_data = []

    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventory WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            read_individual_data.append(row)
            
    return read_individual_data
