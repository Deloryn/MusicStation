from os import path, urandom

from flask import Flask, render_template, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music_station.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = urandom(24)


db = SQLAlchemy()
db.app = app
db.init_app(app)
loginManager = LoginManager()
loginManager.init_app(app)
bcrypt = Bcrypt()
app.static_path = path.join(path.abspath(__file__), 'static')


from models import Song  # Don't move it to the top!


@app.route('/')
def index():
    songs = Song.query.order_by(Song.times_played)[::-1]
    return render_template("index.html", songs=songs)


@app.route('/set_song', methods=["POST"])
def set_song():
    song_path = request.form["track"]
    chosen_song = Song.query.filter(Song.path == song_path).first()
    chosen_song.times_played += 1
    db.session.commit()
    # TODO: set this song for raspberry pi - for example: set_for_raspberry_pi(song_path)
    songs = Song.query.order_by(Song.times_played)[::-1]
    return render_template("index.html", songs=songs)


if __name__ == '__main__':
    app.run(debug=True)
