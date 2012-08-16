from sandbox_web import app
from api import blog
from flask import session, render_template


@app.route('/blog/<blog_id>', methods=['GET'])
def view_blog(blog_id):
    print "view_blog"
    if not session.get('logged_in'):
        abort(401)

    return render_template("show_entries.html", 
                            entries=blog.get_blog(blog_id))

@app.route('/add', methods=('POST') )
def add_blog():
    if not session.get('logged_in'):
        abort(401)

@app.route('/edit', methods=('POST') )
def edit_blog():
    if not session.get('logged_in'):
        abort(401)

@app.route('/del', methods=('POST') )
def delete_blog():
    if not session.get('logged_in'):
        abort(401)



