from flask import Flask

app = Flask(__name__)

@app.route("/")
def hi():
	return "hi!"

@app.route("/hello")
def hello_world():
	return "hello, world!"

@app.route("/test/<search_query>")
def search(search_query):
	return "Hello"+search_query

@app.route("/integer/<int:value>")
def int_type(value):
	print value+1
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print value+1
	return "correct"

@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"

if __name__ == "__main__":
	app.run()