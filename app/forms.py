from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, SelectField, \
    DateField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, Artist


class CreateArtistForm(FlaskForm):
    artist_name = StringField('Artist Name', validators=[DataRequired()])
    artist_hometown = StringField('Hometown')
    artist_genre = StringField('Genre')
    artist_description = TextAreaField('Description')
    submit = SubmitField('Create New Artist')


class CreateVenueForm(FlaskForm):
    venue_name = StringField('Venue Name', validators=[DataRequired()])
    venue_address = StringField('Address', validators=[DataRequired()])
    venue_city = StringField('City', validators=[DataRequired()])
    venue_state = StringField('State (2 letters e.g., NY, NC)', validators=[DataRequired()])
    max_capacity = IntegerField('Max Capacity')
    venue_description = TextAreaField('Description')
    submit = SubmitField('Create New Venue')


class CreateEventForm(FlaskForm):
    event_name = StringField('Event Name', validators=[DataRequired()])
    event_date = DateField('Date', format='%Y-%m-%d')
    event_description = TextAreaField('Description')
    artists = SelectMultipleField('Artists', coerce=int)
    venue = SelectField('Venue', coerce=int)
    submit = SubmitField('Create New Event')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(user_email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

