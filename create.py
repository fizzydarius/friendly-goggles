import sqlite3
from data import Data

conn = sqlite3.connect("database.db")

c = conn.cursor()

c.execute("""CREATE TABLE database (
    username text,
    password text,
    balance integer
        )""")