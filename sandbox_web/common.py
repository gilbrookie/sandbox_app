import conf
import sqlite3

def load_database():
    if not conf.DB_TYPE and not conf.DB_LOC:
        print "Unable to acquire database - check your config"

def connect_db():
    return sqlite3.connect(conf.DB_LOC)

def query_db(db, query, args=(), one=False):
    cur = db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

"""
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()
"""
