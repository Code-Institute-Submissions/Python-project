import os
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret123string"

@app.route("/", methods = ["GET", "POST"])
def index():
    """Welcome / sign in page"""
    if request.method == "POST":
        session["username"] = request.form["username"]
    if "username" in session:
        return render_template("game.html")
    return render_template("index.html")
    
@app.route("/game")
def game():
    """Main game page"""
    return render_template("game.html")
    
@app.route("/leaderboard")
def leaderboard():
    """Show leaderboard page"""
    return render_template("leaderboard.html")

if __name__ == "__main__":
    app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)