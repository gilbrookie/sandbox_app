from datetime import datetime

from api import db

def get_blog(blog_id=None):
    """Returns blog entries from the database as a dictionary.  If id is present then only that
    entry is returns.

    If id does not match anything, the return dict will be empty.
    """
    
    SQL = """
        SELECT title, text, type, created, id
        FROM entries
        """

    conn = db.connect_db()
    cur = conn.cursor()
    res = cur.execute(SQL)
    entries = [dict(title=row[0], 
                    text=row[1], 
                    type=row[2], 
                    created=row[3],
                    id=row[4]) \
                    for row in res.fetchall()]
    
    return entries

def add_blog(blog_vals):
    """Adds a new blog entry to the database"""

    values = [  blog_vals['title'],
                blog_vals['text'],
                blog_vals['type'],
                datetime.now() ]

    SQL = """
        INSERT INTO entries (title, text, type, created
        VALUES (?, ?, ?, ?, ?)"""

    conn = db.connect_db()
    cur = conn.execute(SQL, values)
    cur.commit()

def delete_blog(id):
    """deletes a specific blog entry from the database"""

    SQL = """DELETE FROM entries WHERE id=?"""

    conn = db.connect_db()
    cur = conn.execute(SQL, [id])
    cur.commit()



