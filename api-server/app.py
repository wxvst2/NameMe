from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/ping')
def ping():
	return jsonify(message = "pong")

if __name__ == '__main__':
    app.run()