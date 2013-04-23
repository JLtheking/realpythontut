import sqlite3 as lite
import sys

merchandise = (
	('A4 lecture pad', 2.60),
	('7-colour sticky note with pen', 4.20),
	('A5 ring book', 4.80),
	('A5 note book with zip bag', 4.60),
	('2B pencil', 0.90),
	('Stainless steel tumbler', 12.90),
)

con = lite.connect('merchandise.db')

with con:
	cur = con.cursor()
	
	cur.execute("DROP TABLE IF EXISTS reps")
	cur.execute("DROP TABLE IF EXISTS merchandise")
	cur.execute("CREATE TABLE merchandise(item_name TEXT, unit_price CURRENCY)")
	cur.executemany("INSERT INTO merchandise VALUES(?,?)", merchandise)
	
	