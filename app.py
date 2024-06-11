from flask import Flask
from api import app

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, Flask!'

if __name__ == '__main__':
	app.run(debug=True)
