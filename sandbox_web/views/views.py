
from sandbox_web import app
from api import register_api
from flask import g, session, redirect, render_template, abort, request, flash, url_for
from flask.views import MethodView

from datetime import datetime



template = 'show_entries.html' 

@app.route('/entry/<int:entry_id>', methods=['GET'])
def get(self, entry_id=None):
    print "GET event"
    if not entry_id:
        return "Must provide entry id of the item you wish to view"

    if not session.get('logged_in'):
        abort(401)

    SQL = """
        SELECT title, text, type, created, id
        FROM entries
        WHERE id=?"""

    cur = g.db.execute(SQL, [entry_id])
    entries = [dict(title=row[0], 
                    text=row[1], 
                    type=row[2], 
                    created=row[3],
                    id=row[4]) \
                    for row in cur.fetchall()]

    return render_template(self.template, entries=entries)

    #return entries[0]['title']
    
@app.route('/entry/', methods=['POST'])
def post(self):
    print "POST"
    if not session.get('logged_in'):
        abort(401)

    print request.path
    g.db.execute('insert into entries (title, text, type, created) values (?, ?, ?, ?)',
                 [request.form['title'], 
                  request.form['text'], 
                  request.form['type'],
                  datetime.now()])
    g.db.commit()
    flash('New entry was successfully posted')
        return redirect(url_for('show_entries'))

@app.route('/entry/del/<entry_id>', methods=['POST'])
def delete(self, entry_id):
    print "Got DELETE Request %s" % entry_id
    if not session.get('logged_in'):
        abort(401)

    #print request.form.get('entry_id')
    #cur = g.db.execute("delete from entries WHERE id=?", [entry_id])
    #g.db.commit()

    print "Delete succeeded"
    flash('Entry %s was successfully deleted' % entry_id)
    return redirect(url_for('show_entries'))

# Register the View
register_api(EntryAPI, 'entry_api', '/entry/', pk='entry_id')
