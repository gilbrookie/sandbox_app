from flask import Flask
from sandbox_app import conf

app = Flask(__name__)

app.config.from_object(conf)
print app.jinja_env.list_templates()
from sandbox_web import views
