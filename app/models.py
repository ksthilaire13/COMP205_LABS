from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# This is a secondary relationship table.
# This table is NOT a class, but can be referenced with relationships
ArtistToEvent = db.Table('artisttoevent',
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.artist_id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.event_id')))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    user_email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User: {}>'.format(self.username)

    def set_password(self, user_password):
        self.password_hash = generate_password_hash(user_password)

    def check_password(self, user_password):
        return check_password_hash(self.password_hash, user_password)


class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(64), index=True, unique=True)
    hometown = db.Column(db.String(64), index=True)
    genre = db.Column(db.String(64), index=True)
    description = db.Column(db.String(128), index=True)

    def __repr__(self):
        return '<Artist: ({}) {}>'.format(self.artist_id,self.artist_name)


class Venue(db.Model):
    venue_id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(64), index=True, unique=True)
    venue_address = db.Column(db.String(64), index=True)
    venue_city = db.Column(db.String(64), index=True)
    venue_state = db.Column(db.String(2), index=True)
    venue_description = db.Column(db.String(128), index=True)
    max_capacity = db.Column(db.Integer, index=True)
    events = db.relationship('Event', backref='venue', lazy='dynamic')

    def __repr__(self):
        return '<Venue: ({}) {}>'.format(self.venue_id,self.venue_name)


class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(64), index=True, unique=True)
    event_date = db.Column(db.String(32), index=True)
    event_description = db.Column(db.String(128), index=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.venue_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    artists = db.relationship("Artist", secondary=ArtistToEvent, backref='events')
    def __repr__(self):
        return '<Event: {}>'.format(self.event_name)

