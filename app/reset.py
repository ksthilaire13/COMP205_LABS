import csv
from werkzeug.security import generate_password_hash
from app import db
from app.models import User, Artist, Event, Venue, ArtistToEvent

def reset_data():
    # with app.app_context():  ## Causes this to run on startup
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()

    ## Reload Users - needed for Foreign Keys
    with open('database_scripts\\users.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)  # used for confirmation
            user = User(
                id=row['user_id'],
                username=row['username'],
                user_email=row['user_email'],
                password_hash=generate_password_hash(row['user_password']))
            db.session.add(user)
            db.session.commit()

    ## Reload Artists
    with open('database_scripts\\artists.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)  # used for confirmation
            artist = Artist(
                artist_id=row['artist_id'],
                artist_name=row['artist_name'],
                hometown=row['hometown'],
                genre=row['genre'],
                description=row['description'])
            db.session.add(artist)
            db.session.commit()

    ## Reload Venues
    with open('database_scripts\\venues.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)  # used for confirmation
            venue = Venue(
                venue_id=row['venue_id'],
                venue_name=row['venue_name'],
                venue_address=row['venue_address'],
                venue_description=row['venue_description'],
                max_capacity=row['max_capacity'])
            db.session.add(venue)
            db.session.commit()

    ## Reload Events
    with open('database_scripts\\events.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)  # used for confirmation
            event = Event(
                event_id=row['event_id'],
                event_name=row['event_name'],
                event_date=row['event_date'],
                event_description=row['event_description'],
                venue_id=row['venue_id'],
                user_id=row['user_id'])
            db.session.add(event)
            db.session.commit()

    # Reload Events
    with open('database_scripts\\artist_to_event.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)  # used for confirmation
            db.session.execute(
                ArtistToEvent.insert().values(event_id=row['event_id'],artist_id=row['artist_id']))
            db.session.commit()