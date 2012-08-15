import conf 
import sqlite3

def connect_db():
    print conf.DATABASE
    return sqlite3.connect(conf.DB_LOC, detect_types=sqlite3.PARSE_DECLTYPES)

def load_database():
    if not conf.DB_TYPE and not conf.DB_LOC:
        print "Unable to acquire database - check your config"

def query_db(db, query, args=(), one=False):
    cur = db.cursor()
    res = cur.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in res.fetchall()]
    return (rv[0] if rv else None) if one else rv

