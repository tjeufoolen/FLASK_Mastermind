from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField
from wtforms.validators import DataRequired


class CreateGameForm(FlaskForm):
    player_name = StringField('Player name',
                              validators=[DataRequired(message="Please enter a player name")])
    amount_of_colors = SelectField('Amount of colors',
                                   choices=[(6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")],
                                   default=6,
                                   coerce=int)
    amount_of_positions = SelectField('Amount of positions',
                                      choices=[(4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")],
                                      default=4,
                                      coerce=int)
    double_colors = RadioField('Allow double color placement',
                               choices=[(1, "Yes"), (0, "No")],
                               default=0,
                               coerce=int)

    def validate(self):
        print('cool!')

        if not FlaskForm.validate(self):
            return False

        result = True

        if not self.double_colors.data:
            if self.amount_of_colors.data < self.amount_of_positions.data:
                result = False
                self.double_colors.errors.append('The amount of colors cannot be lower then the amount of '
                                                 'positions while using double colors is disabled.')

        return result
