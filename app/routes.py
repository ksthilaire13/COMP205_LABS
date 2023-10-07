from turtle import pd
from flask import render_template, flash, redirect, url_for, request
from sqlalchemy import select
from app import app, db
from app.forms import CreateArtistForm
from app.models import User, Artist, Event, Venue, ArtistToEvent
from app.reset import reset_data


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
        #artists_list.append({'artist': form.artist_name.data, 'hometown': form.artist_hometown.data,
                           #  'description': form.artist_description.data, 'events': ['none']})
        #return render_template('artist_page.html', title='Artist Page', user=form.artist_name.data + ",",
                            #   posts=artists_list)
    return render_template('new_artist.html', title="New Artist", form=form)


@app.route('/artist_page')
def artist_page():
    artist_id = request.args.get('artist_id')
    artist = Artist.query.get(artist_id)
    events = Event.query.all()
    all_venues = Venue.query.all()
    artist_to_event = ArtistToEvent.query.all()
    this_artist_events = []
    for i in range(len(artist_to_event)):
        if artist_to_event[i].artist_id == artist.artist_id:
            this_artist_events.append(artist_to_event[i])
    the_events = []
    for j in range(len(this_artist_events)):
        for i in range(len(events)):
            if events[i].event_id == this_artist_events[j].event_id:
                the_events.append(events[i])
    artist_venues = []
    for k in range(len(the_events)):
        for l in range(len(all_venues)):
            if all_venues[l].venue_id == the_events[k].venue_id:
                artist_venues.append(all_venues[l])
    event_count = len(the_events)

    return render_template('artist_page.html', title='Artist Page', this_artist=artist_id, artist=artist, events=the_events, event_count=event_count, venues=artist_venues)


@app.route('/reset_db')
def reset_db():
    flash("Resetting database: deleting old data and repopulating with dummy data")
    # clear all data from all tables - in a separate file...
    reset_data()
    return redirect('/')
