from flask import Blueprint, render_template

home = Blueprint('home', __name__)


@home.route('/')
def home():
    return render_template('home/index.html')


@home.route('/home/about')
def about():
    return render_template('profile/photos.html')

