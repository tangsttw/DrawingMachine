import sqlite3
import csv

# open sql script and create sqlite3 data base
with open('create_db.sql') as f:
    create_db_sql = f.read()
db = sqlite3.connect('items.db')
with db:
    db.executescript(create_db_sql)