from flask import Flask
from .views.home import home
from .views.profile import profile

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(profile)
