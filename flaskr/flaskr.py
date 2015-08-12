#coding=utf-8
import sqlite3
from flask import Flask,request,session,g,redirect,url_for,\
abort ,render_template,flash
from contextlib import closing

#configuration
DATABASE="/tmp/flaskr.db"
DEBUG=True
SECRET_KEY="3.1415926"
USERNAME="admin"
PASSWORD="default"


#create app
app=Flask(__name__)

#加载配置
app.config.from_object(__name__)

#数据库准备
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db :
		with app.open_resource("schema.sql") as f :
			db.cursor().executescript( f.read() )
		db.commit()

#优雅的打开关闭数据库
@app.befor_request
def befor_request():
	g.db=connect_db()

@app.teardown_request
def teatdown_request():
	g.db.close()

#视图函数
@app.route("/")
def show_entries():
	cur=g.db.execute("select title,text from entries order by id desc")
	entries=[dict(title=row[0]]





if __name__=="__main__":
	# init_db()
	app.run()


