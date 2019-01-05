from sqlalchemy import Column
from sqlalchemy.types import Integer

from app import db


class Song(db.Model):
    __tablename__ = 'songs'
    path = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    times_played = Column(Integer, default=0)

    def get(self):
        return str(self)
