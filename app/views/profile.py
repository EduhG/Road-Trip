from flask import Blueprint, render_template

profile = Blueprint('profile', __name__)


@profile.route('/<username>')
def profile():
    return render_template('profile/profile.html')


@profile.route('/<username>/photos')
def photos():
    return render_template('profile/photos.html')


@profile.route('/<username>/events')
def profile():
    return render_template('profile/events.html')
