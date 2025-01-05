from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    html = ""
    home = ""
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    with open("home.html", "r", encoding="utf-8") as f:
        home = f.read()
    return html.replace("<txt/>", home)


@app.route("/member")
def member():
    html = ""
    member = ""
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    with open("member.html", "r", encoding="utf-8") as f:
        member = f.read()
    return html.replace("<txt/>", member)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
