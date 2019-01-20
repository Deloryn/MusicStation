__author__ = 'Krzysztof Michalak'

from sqlalchemy import create_engine
from app import db, Song


def db_start():
    create_engine('sqlite:///tmp/music_station.db', convert_unicode=True)
    db.create_all()
    db.session.commit()

    # TODO: you can "add" information about songs here
    song1 = Song()
    song1.path = "path1..."
    song1.name = "name1..."
    db.session.add(song1)

    song2 = Song()
    song2.path = "path2..."
    song2.name = "name2..."
    db.session.add(song2)

    db.session.commit()


if __name__ == '__main__':
    db_start()
