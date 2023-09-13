from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import CreateArtistForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/artists')
def artists():
    return render_template('artists.html', title='Artists', posts=artists_list)


@app.route('/new_artist')
def new_artist():
    form = CreateArtistForm()
    if form.validate_on_submit():
        flash('New Artist Created: {}'.format(
            form.artist_name.data))
        return redirect(url_for('artist_v2.html'), info=form)
    return render_template('new_artist.html', title="New Artist", form=form)


@app.route('/artist_page')
def artist_page():
    my_var = request.args.get('my_var')
    return render_template('artist_page.html', title='Artist Page', user=my_var, posts=artists_list)


artists_list = [
    {
        'artist': 'John Brown\'s Body',
        'description': 'Description wooooo!',
        'events': ['an event', 'another event']
    },
    {
        'artist': 'The Gunpoets',
        'description': 'Voice as a weapon, words as bullets, spreading the universal message of peace, love, and justice through music. Sure, there\'s a cynical cultural tendency to make certain assumptions when you hear the word \"gun\" associated with rap music, but this seven-member live hip-hop band from Ithaca, NY, runs contrary to that image with their positive message and uplifting performances.',
        'events': ['The Haunt next Friday 9/14', 'The Commons on Thursday 9/6'],
    },
    {
        'artist': 'Donna The Buffalo',
        'description': 'Description blah blah blah',
        'events': ['event 1', 'event 2']
    },
    {
        'artist': 'The Blind Spots',
        'description': 'Description blah blah blah pt 2',
        'events': ['event 3', 'event 4']
    }
]
