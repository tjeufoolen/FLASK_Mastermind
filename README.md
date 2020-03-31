# PYTHON-Mastermind
Assessment python blok 7

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
Automatic rebuilding on code change:

Linux/MacOS
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Windows
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

## Authors
- [Micha Nijenhof](https://github.com/killermi200)
- [Tjeu Foolen](https://github.com/tjeufoolen)
