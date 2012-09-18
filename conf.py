import os
# Database Type
DB_TYPE = "SQLite"

# Location of the database
DB_LOC  = "/var/www/sandbox_app/test.db"

# FOR TESTING - REINITIALIZE DB when launching app
# For production, set to False (which is default)
DB_REINIT = True

DATABASE = DB_LOC
DEBUG = True
SECRET_KEY = "Devkey123"
USERNAME = 'admin'
PASSWORD = 'admin'

