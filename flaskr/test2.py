#coding=utf-8

import sqlite3
connect=sqlite3.connect("temp.db")
cur=connect.cursor()


cur.execute("drop table names")

cur.execute('''
	create  table if not exists names(
		ids integer,
		name string not null,
		primary key (ids) )
	''')

names=[(1,"leilei"),(2,"sisi"),(3,"nice")]

cur.execute("insert into names values(?,?)",(5,"you should marry with me!") )
cur.executemany("insert into  names values(?,?)",names)

# connect.commit()

cur.execute("select * from names")
for i,n in cur.fetchall():
	print i,n

# connect.commit()

cur.close()
connect.close()