from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class MovieForm(FlaskForm):
    movie_name = StringField("Movie Title")
    rel_yr = IntegerField("Year of Release")
    dir_name = StringField("Director")
    submit = SubmitField("Submit")