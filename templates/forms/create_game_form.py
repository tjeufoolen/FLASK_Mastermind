from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField
from wtforms.validators import DataRequired


class CreateGameForm(FlaskForm):
    player_name = StringField('Player name', validators=[DataRequired(message="Please enter a player name")])
    amount_of_colors = SelectField('Amount of colors',
                                   choices=[(6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")], default=6,
                                   coerce=int)
    amount_of_positions = SelectField('Amount of positions',
                                      choices=[(4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")],
                                      default=4, coerce=int)
    double_colors = RadioField('Allow double color placement', choices=[(True, "Yes"), (False, "No")], default=False,
                               coerce=bool)
