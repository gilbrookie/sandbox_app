
import os
from pprint import pprint as pp

import api
from sandbox_web import app

from flask import g, session, redirect, render_template, abort, \
                    request, flash, url_for, send_from_directory


@app.route("/")
def home():
    """This function peforms the home page view"""
    pp(api.blog.get_blog())
    return render_template("show_entries.html", 
                            entries=api.blog.get_blog())

@app.route("/login", methods=["GET", "POST"])
def login():
    pass

@app.route("/logout")
def logout():
    pass

@app.route("/file/<path:filename>")
def get_file(filename):
    """This function serves file from the file_store directory;
    Returns the file provided by the path:filename argument"""

    print app.config
    return send_from_directory(os.getcwd()+"/file_store/", 
                               filename, as_attachment=True)

@app.route("/file/")
@app.route("/files/")
def list_files():
    """Lists all files available in the filestore"""
    return render_template("files.html", 
                            file_list=os.listdir(os.getcwd()+"/file_store/")) 
