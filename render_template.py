# This code returns a html template
from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("render_template.html")
if __name__ == '__main__':
    app.run(debug=True)