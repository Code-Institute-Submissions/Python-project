import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/game")
def game():
    return render_template("game.html")
    
@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")

if __name__ == "__main__":
    app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)