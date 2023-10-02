from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True)
    user_email = db.Column(db.String(128), index=True, unique=True)
    user_password = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        return '<User: {}>'.format(self.venue_name)


class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(128), index=True, unique=True)
    hometown = db.Column(db.String(128), index=True, unique=True)
    genre = db.Column(db.String(128), index=True, unique=True)
    description = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '<Artist: {}>'.format(self.artist_name)


class Venue(db.Model):
    venue_id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(128), index=True, unique=True)
    venue_address = db.Column(db.String(128), index=True, unique=True)
    venue_description = db.Column(db.String(128), index=True, unique=True)
    max_capacity = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '<Venue: {}>'.format(self.venue_name)


class Event(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(128), index=True, unique=True)
    hometown = db.Column(db.String(128), index=True, unique=True)
    genre = db.Column(db.String(128), index=True, unique=True)
    description = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '<Event: {}>'.format(self.venue_name)