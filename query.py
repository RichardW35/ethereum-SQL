import sqlite3 as sq3

conn = sq3.connect("blockchain.db")
cur = conn.cursor()

# some SQL code, e.g. select first five entries of the table Quick
cur.execute("SELECT * FROM foreverstrong LIMIT 5")
a = cur.fetchall()  #list of tuples containing all elements of the row
print(a)
conn.close()