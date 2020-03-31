import settings
from database.database import Database
from flask import Flask, render_template, request, redirect, url_for, abort
from templates.forms import CreateGameForm
from models import Game, Player, GameTurn

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


@app.route('/game/<id>', methods=["GET", "POST"])
def game(id):
    g = db.get_game(id)

    if not g:
        abort(404)

    # Redirect back to home if already completed
    if g.completed_at:
        return redirect(url_for('home'))

    if request.method == 'POST':

        # Validate input
        code_guessed = [string for string in request.form.getlist('answer[]') if string != "" and string in g.color_options]
        if len(code_guessed) == g.amount_of_positions:
            turn = GameTurn(game_id=id, code_guessed=code_guessed)
            db.create_game_turn(turn)

            # Check if player won
            if turn.code_guessed == g.code:
                db.set_game_completed(g.id)
                return redirect(url_for('win', id=g.id))

            return redirect(url_for('game', id=g.id))

    return render_template('game.html', game=g, cheatmode=settings.CHEAT_MODE)


@app.route('/win/<id>', methods=["GET"])
def win(id):
    g = db.get_game(id)

    if not g or not g.completed_at:
        abort(404)

    return render_template('win.html', game=g)


@app.route('/leaderboard')
def leaderboard():
    top_games = db.get_top_games()
    top_players = db.get_top_players()

    return render_template('leaderboard.html', games=top_games, players=top_players)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
