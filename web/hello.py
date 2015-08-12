#coding=utf-8
import IPython
from flask import Flask,url_for,render_template\
,redirect,abort,request,escape




app=Flask(__name__)
# app.debug=True

#重定向
@app.route('/login/',methods=['POST', 'GET'])
def login():
	# abort(401)
	# return redirect(url_for('hello'))
	return "login : %s "%request.method


#------------------------------------------------------------------------------------------------------
#渲染模板
# @app.route('/hello/')
@app.route('/hello/<name>/',methods=['post','get'] )
def hello(name):
	s=request.method
	# d={"username":name,"key":"3.1415926"}
	s+=url_for(hello.__name__ , name="leilei",key="3.1415926"  )
	app.logger.debug(name)
	
	return s
	# IPython.embed()
	# return render_template("hello.html",name=name)

#------------------------------------------------------------------------------------------------------
#调试模式
@app.route('/')
def hello_world():
	s=u'''
	红豆
		——王维
	红豆生南国，
	春来发几枝。
	愿君多采撷，
	此物最相思。
	'''		
	s+=request.path
	# raise Exception ,"debug... ..."    	#app.debug=True
	return  s

#--------------------------------------------------------------
# url变量
# @app.route("/user/<username>/")
# def profile(username):
# 	with app.test_request_context():		
# 		return "hello %s from %s"%(username,url_for("profile", username='%s'%username) )
# 	pass

@app.route("/post/<path:post_id>/")
def show_post3(post_id):
	return "post3: %s"%post_id

# @app.route("/post/<int:post_id>")
# def show_post1(post_id):
# 	return "post1: %d"%post_id

# @app.route("/post/<float:post_id>")
# def show_post2(post_id):
# 	return "post2: %f"%post_id


#This has to be executed when application context is available.
# print url_for("login") 

# with app.test_request_context():
# 	# print url_for('hello')
# 	# print url_for('show_post2',post_id=564509)
# 	print url_for('login', next='/')
# 	# print url_for('profile')
# 	IPython.embed()



# import ipdb
# ipdb.set_trace()




# with app.test_request_context('/hello', method='POST'):
# 	print dir()

if __name__=='__main__':	
	app.run()

