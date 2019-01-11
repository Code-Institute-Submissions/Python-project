import os
import json
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "secret123string")


@app.route("/", methods = ["GET", "POST"])
def index():
    """Welcome / sign in page"""
    if request.method == "POST":
        session["username"] = request.form["username"]
    if "username" in session:
        return redirect(url_for("game"))
    return render_template("index.html")


@app.route("/game")
def game():
    """Main game page"""
    riddles = []
    with open("data/riddles.json", "r") as json_data:
        riddles = json.load(json_data)
    return render_template("game.html", riddle = riddles[0])
    
    
@app.route("/leaderboard")
def leaderboard():
    """Show leaderboard page"""
    return render_template("leaderboard.html")

if __name__ == "__main__":
    app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)