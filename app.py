from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.route("/about")
def about():
    with open("about.html", "r", encoding="utf-8") as f:
        return f.read()


@app.route("/works")
def works():
    with open("work.html", "r", encoding="utf-8") as f:
        return f.read()


app.run(debug=True, host="0.0.0.0")
