""" Flask code that prints hello world in Browser"""
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug = True)