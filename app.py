import settings
from database.database import Database
from flask import Flask, render_template, request, redirect, url_for, abort
from templates.forms import CreateGameForm
from models import Game, Player

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
db = Database(settings.DATABASE_FILE)


@app.route('/', methods=["GET", "POST"])
def home():
    form = CreateGameForm()

    if request.method == 'POST' and form.validate():
        g = Game(player=Player(form.player_name.data),
                 double_colors=form.double_colors.data,
                 amount_of_colors=form.amount_of_colors.data,
                 amount_of_positions=form.amount_of_positions.data)

        g.id = db.create_game(g)
        return redirect(url_for('game', id=g.id))

    return render_template('index.html', form=form)


@app.route('/game/<id>', methods=["GET"])
def game(id):
    g = db.get_game(id)

    if not g:
        abort(404)

    return render_template('game.html')


@app.route('/win')
def win():
    return render_template('win.html')


@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
