from flask import Blueprint, render_template

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/')
def index():
    return render_template('home/index.html')


@home_blueprint.route('/home/about')
def about():
    return render_template('home/about.html')

