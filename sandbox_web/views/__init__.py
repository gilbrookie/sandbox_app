
import api
from sandbox_web import app
from flask import g, session, redirect, render_template, abort, request, flash, url_for
from pprint import pprint as pp

@app.route("/")
def home():
    pp(api.blog.get_blog())
    return render_template("show_entries.html", entries=api.blog.get_blog())

@app.route("/login", methods=["GET", "POST"])
def login():
    pass

@app.route("/logout")
def logout():
    pass


