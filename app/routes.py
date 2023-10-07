from turtle import pd
from flask import render_template, flash, redirect, url_for, request
from sqlalchemy import select
from app import app, db
from app.forms import CreateArtistForm
from app.models import User, Artist, Event, Venue, ArtistToEvent


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/artists')
def artists():
    artists = Artist.query.all()
    return render_template('artists.html', title='Artists', artists=artists)


@app.route('/new_artist', methods=['GET', 'POST'])
def new_artist():
    form = CreateArtistForm()
    if form.validate_on_submit():
        flash('New Artist Created: {}'.format(form.artist_name.data))
        artists_list.append({'artist': form.artist_name.data, 'hometown': form.artist_hometown.data,
                             'description': form.artist_description.data, 'events': ['none']})
        return render_template('artist_page.html', title='Artist Page', user=form.artist_name.data + ",",
                               posts=artists_list)
    return render_template('new_artist.html', title="New Artist", form=form)


@app.route('/artist_page')
def artist_page():
    artist_id = request.args.get('artist_id')
    artist = Artist.query.get(artist_id)
    artist_to_event = ArtistToEvent.query.all()
    #print(artist)
    #print(ArtistToEvent.query.get(artist_id))
    #event_id_list = ArtistToEvent.query.filter(ArtistToEvent.artist_id == Artist.artist_id)
    # event_id_list = select()
    #print(event_id_list)
    #event_list = Event.query.filter(Event.event_id == event_id_list.event_id)
    #print(event_list)
    return render_template('artist_page.html', title='Artist Page', this_artist=artist_id, artist=artist, artist_events=artist_to_event)


@app.route('/reset_db')
def reset_db():
    flash("Resetting database: deleting old data and repopulating with dummy data")
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()

    df = pd.read_csv('artists.csv')
    df.to_sql('Artists_1', db.engine, if_exists='replace', index=False)

    df = pd.read_csv('events.csv')
    df.to_sql('Events_1', db.engine, if_exists='replace', index=False)

    df = pd.read_csv('users.csv')
    df.to_sql('Users_1', db.engine, if_exists='replace', index=False)

    df = pd.read_csv('venues.csv')
    df.to_sql('Venues_1', db.engine, if_exists='replace', index=False)


artists_list = [
    {
        'artist': 'Johnny Cakes',
        'hometown': 'Ithaca',
        'description': 'Description wooooo!',
        'events': ['an event', 'another event']
    },
    {
        'artist': 'John Brown\'s Body',
        'hometown': 'Ithaca',
        'description': 'Description wooooo!',
        'events': ['an event', 'another event']
    },
    {
        'artist': 'The Gunpoets',
        'hometown': 'Ithaca',
        'description': 'Voice as a weapon, words as bullets, spreading the universal message of peace, love, and justice through music. Sure, there\'s a cynical cultural tendency to make certain assumptions when you hear the word \"gun\" associated with rap music, but this seven-member live hip-hop band from Ithaca, NY, runs contrary to that image with their positive message and uplifting performances.',
        'events': ['The Haunt next Friday 9/14', 'The Commons on Thursday 9/6'],
    },
    {
        'artist': 'Donna The Buffalo',
        'hometown': 'Ithaca',
        'description': 'Description blah blah blah',
        'events': ['event 1', 'event 2']
    },
    {
        'artist': 'The Blind Spots',
        'hometown': 'Ithaca',
        'description': 'Description blah blah blah pt 2',
        'events': ['event 3', 'event 4']
    }
]
