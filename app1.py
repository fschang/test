# ---- Flask Hello World ---- #

#import the Flas class from the flask module

from flask import Flask

# create the application object

app = Flask(__name__)

#use decorators to link the function to a url

@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string
def hello_world():
	return "Hello, World!"

@app.route("/faggot")
@app.route("/faggot1")
def faggot():
	return "faggot"

#dynamic route
@app.route("/test")
def bye():
	return "Hello"
'''
@app.route("/test/<search_query>")
def search(search_query):
	return search_query
'''
@app.route("/test/<int:numberx2>")
def wtf(numberx2):
	print numberx2*2
	return numberx2*2, 200

# start the development server using the run() method
if __name__ == "__main__":
	app.run()