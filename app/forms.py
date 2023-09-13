from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class CreateArtistForm(FlaskForm):
    artist_name = StringField('Artist Name', validators=[DataRequired()])
    artist_hometown = StringField('Hometown')
    artist_description = StringField('Description')
    submit = SubmitField('Create New Artist')
