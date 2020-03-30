import settings
from database.database import Database
from flask import Flask, render_template, request, redirect
from templates.forms import CreateGameForm

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
db = Database(settings.DATABASE_FILE)


@app.route('/', methods=["GET", "POST"])
def home():
    form = CreateGameForm()

    if request.method == 'POST' and form.validate():
        return redirect('/game')

    return render_template('index.html', form=form)


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/win')
def win():
    return render_template('win.html')


@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')
