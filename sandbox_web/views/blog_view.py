from sandbox_web import app
from api import blog


@app.route('/blog')
def view_blog():
    if not session.get('logged_in'):
        abort(401)

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



