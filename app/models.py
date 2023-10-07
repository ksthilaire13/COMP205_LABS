# import export
# import flask
from datetime import datetime
from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    user_email = db.Column(db.String(64), index=True, unique=True)
    user_password = db.Column(db.String(32), index=True, unique=False)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(64), index=True, unique=True)
    hometown = db.Column(db.String(64), index=True)
    genre = db.Column(db.String(64), index=True)
    description = db.Column(db.String(128), index=True)

    def __repr__(self):
        return '<Artist: {}>'.format(self.artist_name)


class Venue(db.Model):
    venue_id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(64), index=True, unique=True)
    venue_address = db.Column(db.String(64), index=True)
    venue_description = db.Column(db.String(128), index=True)
    max_capacity = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Venue: {}>'.format(self.venue_name)


class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(64), index=True, unique=True)
    event_date = db.Column(db.String(32), index=True)
    event_description = db.Column(db.String(128), index=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.venue_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __repr__(self):
        return '<Event: {}>'.format(self.event_name)


class ArtistToEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))

    def __repr__(self):
        return '<Artist To Event ID: {}>'.format(self.id)

