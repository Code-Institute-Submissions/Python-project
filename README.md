# Practical Python Project

## Riddle Me This Web Application Game

The Riddle Me This web application allows multiple individual potential players to sign into the
riddle guessing game. A unique personalised game playing page is then accessed, where riddles are
asked and answers obtained. The answers given are evaluated, either right or wrong, and points awarded
depending on the number of guesses required to answer the riddle correctly. Points are accumulated
through playing the game, which are displayed on the separate leaderboard page. The leaderboard page also
provides the option to quit or log out of the game when complete.

Wireframes for this web application can be accessed [here](/python_project_wireframes)

### Technologies Used

[HMTL5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
   * Used to define the web application.

[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
   * Used to apply styles and colours to, and provide a responsive layout for the web application.

[Python](https://www.python.org/)
   * Used to code the application's logic and data processing needs.

[Flask](http://flask.pocoo.org/)
   * A web framework used with Python programming language.

### Testing

Potential players can sign in at the initial screen for the Riddle Me This web application. Clicking on
the 'Play the Game' button brings the player to a personalised game page where they are greeted with the 
name supplied previously. This functionality was tested by supplying different usernames to the sign in page
and ensuring the game page displayed the correct username.

The riddle guessing game was tested by answering a riddle correctly and ensuring that the correct response was 
displayed and the score was incremented by the appropriate number of points. The 'Next Riddle' button brings the 
player to the next riddle.
A wrong answer was supplied to ensure the correct response was displayed, along with the wrong answer that was supplied.
The correct answer was then supplied to ensure the correct response was displayed and the score was incremented
by the appropriate number of points. The 'Next Riddle' button brings the player to the next riddle.
A wrong answer was supplied on two occassions to ensure the correct response was displayed each time, along with
the wrong answer that was supplied on each occassion. The correct answer was then supplied to ensure the correct response
was displayed and the score was incremented by the appropriate number of points. The 'Next Riddle' button brings
the player to the next riddle.
Finally, a wrong answer was provided on three occassions to ensure the correct responses were displayed and a prompt
to try the next riddle was displayed on final wrong answer.The 'Next Riddle' button brings the player to the next riddle.
An additional test was performed with the correct answer being supplied either capitalized, or in full capitals, to 
ensure that this answer was still evaluated correctly.
The 'Show Leaderboard' button directs the player to the Leaderboard Page.

The Leaderboard Page displays a leaderboard with the player's name as provided at the sign in page, ranked according
to the score achieved by playing the game. Different names and scores were used to test this functionality. 
The 'Back to Game' button returns the player to the Game Page and the 'Quit Game' button clears the username 
stored in the session and returns the player back to the Sign in Page.

The web application was tested for full operation as above and once rendered in a browser window, the browser
window was re-sized to prove the responsive, mobile first design of the webpage.

### Deployment

The web application is deployed on heroku here https://riddle-me-this-gd.herokuapp.com
The code can be found on Github here https://github.com/GeoffDoig/Python-project