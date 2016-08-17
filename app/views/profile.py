from flask import Blueprint, render_template

profile_blueprint = Blueprint('profile', __name__)


@profile_blueprint.route('/<username>')
def profile(username):
    return render_template('profile/profile.html')


@profile_blueprint.route('/<username>/photos')
def photos(username):
    return render_template('profile/photos.html')


@profile_blueprint.route('/<username>/events')
def events(username):
    return render_template('profile/events.html')
