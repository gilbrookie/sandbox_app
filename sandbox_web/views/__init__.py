
import api, conf
from sandbox_web import app
from flask import g, session, redirect, render_template, abort, request, flash, url_for
from pprint import pprint as pp

import blog_view


@app.route("/")
def home():
    pp(api.blog.get_blog())
    return render_template("show_entries.html", entries=api.blog.get_blog())

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != conf.USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != conf.PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries.html'))


