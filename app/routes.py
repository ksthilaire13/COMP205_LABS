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
    artists = Artist.query.all()
    copy = False
    form = CreateArtistForm()
    if form.validate_on_submit():
        for i in range(len(artists)):
            if form.artist_name.data in artists[i].artist_name:
                flash('Sorry! That artist already exists')
                copy = True
                return redirect('/artists')
        if copy is False:
            flash('New Artist Created: {}'.format(form.artist_name.data))
            artist = Artist(
                artist_name=form.artist_name.data,
                hometown=form.artist_hometown.data,
                genre=form.artist_genre.data,
                description=form.artist_description.data)
            db.session.add(artist)
            db.session.commit()
            return redirect('/artists')
    return render_template('new_artist.html', title="New Artist", form=form)


@app.route('/artist_page/<artist_name>')
def artist_page(artist_name):
    artist = Artist.query.filter_by(artist_name=artist_name).first_or_404()
    the_events = artist.events
    event_count = len(the_events)
    return render_template('artist_page.html', title='Artist Page',
                           artist=artist, events=the_events, event_count=event_count)


@app.route('/reset_db')
def reset_db():
    flash("Resetting database: deleting old data and repopulating with dummy data")
    # clear all data from all tables - in a separate file...
    reset_data()
    return redirect('/')
