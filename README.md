# FLASK_Mastermind
Mastemind the game build using python and flask

## Prerequisites
- virtualenvironment (venv)
- pip packages
    - Flask
    - Flask-WTF
    - python-dotenv

## Getting Started
1. Clone this repository.
2. Create a `mastermind.db` file inside the `storage` folder.
3. Execute the sql from `storage/mastermind.sql` onto the `mastermind.db` you just created.
4. Copy and rename `.env.example` to `.env`.
5. Fill in your credentials inside the `.env`.
6. Run the flask program. (For tips on how to checkout the #Development tips below)
7. Enjoy! :tada:
    
## Development tips
To enable automatic rebuilding on code change, set the current flask app to run in a dev environment.
See the code examples below for more information on how to set this up on windows or unix.

**Unix**
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

**Windows**
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

## Authors
- [Micha Nijenhof](https://github.com/killermi200)
- [Tjeu Foolen](https://github.com/tjeufoolen)
