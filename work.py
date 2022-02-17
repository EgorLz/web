from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)


@app.route('/profile/<username>/<int:number>')
def index(username, number):
    params = {
        "username": username,
        "number": number,
        "title": "Home Page"
    }
    return render_template("index.html", **params)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')