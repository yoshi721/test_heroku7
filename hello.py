from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello  World. THIS IS A NEW TEST!'