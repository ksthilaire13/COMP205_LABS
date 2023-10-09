from turtle import pd
from flask import render_template, flash, redirect, url_for, request
from sqlalchemy import select
from werkzeug.urls import url_parse

from app import app, db
from app.forms import CreateArtistForm, LoginForm, RegistrationForm
from app.models import User, Artist, Event, Venue, ArtistToEvent
from app.reset import reset_data
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/artists')
def artists():
    artists = Artist.query.all()
    return render_template('artists.html', title='Artists', artists=artists)


@app.route('/new_artist', methods=['GET', 'POST'])
@login_required
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, user_email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
