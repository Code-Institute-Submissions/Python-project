import os
from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "secret123string")

wrong_answer = []
riddles = []
answers = []
scores = []

def read_data():
    with open("data/riddles.txt", "r") as file:
        lines = file.read().splitlines()
    for n, text in enumerate(lines):
        if n%2 == 0:
            riddles.append(text)
        else:
            answers.append(text)

def process_answer(answer):
    if request.method == "POST":
        response = request.form["answer"]
        if response.lower() == answer and session["attempt"] == 0:
            flash("That's correct! You scored 5 points!")
            session["score"] += 5
            session["number"] += 1
        elif response.lower() != answer and session["attempt"] == 0:
            flash("Sorry, that's not right! Please try again")
            session["attempt"] += 1
            wrong_answer.append(response)
        elif response.lower() == answer and session["attempt"] == 1:
            flash("That's correct! You scored 3 points!")
            session["score"] += 3
            session["number"] += 1
            session["attempt"] = 0
            wrong_answer.pop()
        elif response.lower() != answer and session["attempt"] == 1:
            flash("Sorry, that's not right! Please try again")
            session["attempt"] += 1
            wrong_answer.append(response)
        elif response.lower() == answer and session["attempt"] == 2:
            flash("That's correct! You scored 1 point!")
            session["score"] += 1
            session["number"] += 1
            session["attempt"] = 0
            remove_wrong_answer()
        else:
            flash("Sorry, that's not right! You have no more attempts, please try the next riddle")
            session["number"] += 1
            session["attempt"] = 0
            remove_wrong_answer()

def remove_wrong_answer():
    wrong_answer.pop(1)
    wrong_answer.pop()
    
@app.route("/", methods = ["GET", "POST"])
def index():
    """Welcome / sign in page"""
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["score"] = 0
        session["number"] = 0
        session["attempt"] = 0
    if "username" in session:
        return redirect(url_for("game", username = session["username"]))
    return render_template("index.html")

@app.route("/game/<username>", methods = ["GET", "POST"])
def game(username):
    """Main game page"""
    read_data()
    if session["number"] < len(riddles):
        answer = answers[session["number"]]
        process_answer(answer)
        return render_template("game.html", riddle = riddles[session["number"]], score = session["score"], wrong_answer = wrong_answer)
    return redirect(url_for("leaderboard"))

@app.route("/leaderboard", methods = ["GET", "POST"])
def leaderboard():
    """Show leaderboard page"""
    if session["number"] >= len(riddles):
        flash("Game Complete! Find your score on the leaderboard")
    username = session["username"]
    score = session["score"]
    scores.append((username, score))
    top_scores = sorted(scores, key = lambda e: e[1], reverse = True)
    return render_template("leaderboard.html", top_scores = top_scores)

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)