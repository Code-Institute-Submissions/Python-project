import os
import json
from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "secret123string")

attempt = 0
score = 0
i = 0
riddles = []
wrong_answer = []

def process_answer(response, answer):
    global attempt
    global score
    global i
    if response.lower() == answer and attempt == 0:
        flash("That's correct! You scored 5 points!")
        score += 5
        i += 1
        return redirect(url_for("game"))
    elif response.lower() != answer and attempt == 0:
        flash("Sorry, that's not right! Please try again")
        attempt += 1
        wrong_answer.append(response)
        return redirect(url_for("game"))
    elif response.lower() == answer and attempt == 1:
        flash("That's correct! You scored 3 points!")
        score += 3
        i += 1
        attempt = 0
        wrong_answer.pop()
        return redirect(url_for("game"))
    elif response.lower() != answer and attempt == 1:
        flash("Sorry, that's not right! Please try again")
        attempt += 1
        wrong_answer.append(response)
        return redirect(url_for("game"))
    elif response.lower() == answer and attempt == 2:
        flash("That's correct! You scored 1 point!")
        score += 1
        i += 1
        attempt = 0
        wrong_answer.pop(1)
        wrong_answer.pop()
        return redirect(url_for("game"))
    else:
        flash("Sorry, that's not right! You have no more attempts, please try the next riddle")
        i += 1
        attempt = 0
        wrong_answer.pop(1)
        wrong_answer.pop()
        return redirect(url_for("game"))
    
@app.route("/", methods = ["GET", "POST"])
def index():
    """Welcome / sign in page"""
    if request.method == "POST":
        session["username"] = request.form["username"]
    if "username" in session:
        return redirect(url_for("game"))
    return render_template("index.html")

@app.route("/game", methods = ["GET", "POST"])
def game():
    """Main game page"""
    with open("data/riddles.json", "r") as data:
        riddles = json.load(data)
        if request.method == "POST":
            response = request.form["answer"]
            answer = riddles[i]["answer"]
            process_answer(response, answer)
    return render_template("game.html", riddle = riddles[i], score = score, wrong_answer = wrong_answer)
    
@app.route("/leaderboard")
def leaderboard():
    """Show leaderboard page"""
    return render_template("leaderboard.html")

if __name__ == "__main__":
    app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)