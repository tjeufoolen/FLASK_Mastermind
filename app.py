from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/win')
def win():
    return render_template('win.html')


@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')
