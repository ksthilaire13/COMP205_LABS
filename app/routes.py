from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/artists')
def artists():
    artists_list = [
        {
            'artist': 'John Brown\'s Body',
            'description': 'Description wooooo!',
            'events': ['an event', 'another event']
        },
        {
            'artist': 'The Gunpoets',
            'description': 'Voice as a weapon, words as bullets, spreading the universal message of peace, love, and justice through music. Sure, there\'s a cynical cultural tendency to make certain assumptions when you hear the word \"gun\" associated with rap music, but this seven-member live hip-hop band from Ithaca, NY, runs contrary to that image with their positive message and uplifting performances.',
            'events': ['The Haunt next Friday 9/14','The Commons on Thursday 9/6'],
        },
        {
            'artist': 'Donna The Buffalo',
            'description': 'Description blah blah blah',
            'events': ['event 1', 'event 2']
        },
        {
            'artist': 'The Blind Spots',
            'description': 'Description blah blah blah pt 2',
            'events': ['event 3, event 4']
        }
    ]
    return render_template('artists.html', title='Artists', posts=artists_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
