from flask import render_template

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # return render_template()
    # return "index"
    return render_template("game.html")

if __name__ == '__main__':
    app.run()


