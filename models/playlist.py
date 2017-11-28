import sqlite3
from db import db

class PlaylistModel(db.Model):
    __tablename__ = 'playlists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(4000))

    def __init__(self, playlist_id, options):
        self.name = options.name
        self.description = options.description

    def json(self):
        return {'name':self.name, 'description':self.description}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()

    # @classmethod
    # def find_by_name(cls, name):
    #     return cls.query.filter_by(name=name).first()
