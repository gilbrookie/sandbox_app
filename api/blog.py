from datetime import datetime

from api import db
from api.status import Status, OK, ERROR

def get_blog(blog_id=None):
    """Returns blog entries from the database as a dictionary.  If id is present then only that
    entry is returns.

    If id does not match anything, the return dict will be empty.
    """
    
    conn = db.connect_db()
    cur = conn.cursor()

    if not blog_id:
        SQL = """
            SELECT title, text, type, created, id
            FROM entries
            """

        res = cur.execute(SQL)

    else:
        SQL = """
            SELECT title, text, type, created, id
            FROM entries
            WHERE id=?
            ORDER BY id desc
            """
        res = cur.execute(SQL, [blog_id])
            
    entries = [dict(title=row[0], 
                    text=row[1], 
                    type=row[2], 
                    created=row[3],
                    id=row[4]) \
                    for row in res.fetchall()]
    
    #status = Status(OK, None)

    return  entries

def add_blog(request_form):
    """Adds a new blog entry to the database"""

    print request_form 
    values = [ request_form['title'], 
               request_form['text'],
               request_form['type'],
               datetime.now() ]

    print values

    SQL = """
        INSERT INTO entries (title, text, type, created)
        VALUES (?, ?, ?, ?)"""

    conn = db.connect_db()
    cur = conn.cursor()
    res = cur.execute(SQL,values)
    conn.commit()

def delete_blog(id):
    """deletes a specific blog entry from the database"""

    SQL = """DELETE FROM entries WHERE id=?"""

    conn = db.connect_db()
    cur = conn.execute(SQL, [id])
    conn.commit()



