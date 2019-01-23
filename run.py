import os
from flask import Flask, render_template, request, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "secret123string")

wrong_answer = []
riddles = []
answers = []
scores = []

def read_data():
    """Read data file and compile riddles and answers lists"""
    with open("data/riddles.txt", "r") as file:
        lines = file.read().splitlines()
    for n, text in enumerate(lines):
        if n%2 == 0:
            riddles.append(text)
        else:
            answers.append(text)

def process_answer(answer):
    """Evaluate answer given by player and award points accordingly"""
    if request.method == "POST":
        response = request.form["answer"]
        if response.lower() == answer and session["attempt"] == 0:
            flash("That's correct! You scored 5 points!", "right")
            session["score"] += 5
        elif response.lower() != answer and session["attempt"] == 0:
            flash("Sorry, that's not right! Please try again", "wrong")
            session["attempt"] += 1
            wrong_answer.append(response)
        elif response.lower() == answer and session["attempt"] == 1:
            flash("That's correct! You scored 3 points!", "right")
            session["score"] += 3
            session["attempt"] = 0
            wrong_answer.pop()
        elif response.lower() != answer and session["attempt"] == 1:
            flash("Sorry, that's not right! Please try again", "wrong")
            session["attempt"] += 1
            wrong_answer.append(response)
        elif response.lower() == answer and session["attempt"] == 2:
            flash("That's correct! You scored 1 point!", "right")
            session["score"] += 1
            session["attempt"] = 0
            remove_wrong_answer()
        else:
            flash("Sorry, that's not right! You have no more attempts, please try the next riddle", "wrong")
            session["attempt"] = 0
            remove_wrong_answer()

def remove_wrong_answer():
    """Stop displaying the wrong answers"""
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
    """Display riddle and evaluate answer given by player"""
    read_data()
    answer = answers[session["number"]]
    process_answer(answer)
    return render_template("game.html", riddle = riddles[session["number"]], score = session["score"], wrong_answer = wrong_answer)
    
@app.route("/next_riddle")
def next_riddle():
    """Increment riddles list index number and display next riddle"""
    session["number"] += 1
    if session["number"] < len(riddles):
        return redirect(url_for("game", username = session["username"]))
    else:
        return redirect(url_for("leaderboard"))

@app.route("/leaderboard", methods = ["GET", "POST"])
def leaderboard():
    """Show leaderboard page"""
    if session["number"] >= len(riddles):
        flash("Game Complete! Find your score on the leaderboard", "end")
    username = session["username"]
    score = session["score"]
    scores.append((username, score))
    top_scores = sorted(scores, key = lambda e: e[1], reverse = True)
    return render_template("leaderboard.html", top_scores = top_scores)

@app.route("/logout")
def logout():
    """Log player out of game and return to sign in page"""
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', '5000')), debug = False)