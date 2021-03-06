from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_game_form():
    """If they want to play MadLibs"""

    choice_for_game = request.args.get("game")

    if choice_for_game == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Play MadLibs!!"""

    choice_color = request.args.get("color")
    choice_noun = request.args.get("noun")
    choice_verb = request.args.getlist("verbs")
    print "*********************************"
    print choice_verb
    choice_adjective = request.args.get("adjective")
    player = request.args.get("person")


    return render_template("madlib.html",
                            color=choice_color,
                            noun=choice_noun,
                            verbs=choice_verb,
                            person=player,
                            adjective=choice_adjective
                            )
if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
