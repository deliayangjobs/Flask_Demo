import sqlite3
from db import db

class TrackModel(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    season = db.Column(db.Integer)
    episode = db.Column(db.Integer)
    status = db.Column(db.String(20))
    pix = db.Column(db.String(1000))
    link = db.Column(db.String(1000))

    playlist = db.Column(db.Integer, db.ForeignKey('playlists.id'))
    playlistModel = db.relationship('PlaylistModel')

    source = db.Column(db.Integer, db.ForeignKey('sources.id'))
    sourceModel = db.relationship('SourceModel')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    userModel = db.relationship('UserModel')

    def __init__(self, options):
        self.name = options.name
        self.season = options.season
        self.episode = options.episode
        self.status = 'ACTIVE'
        self.pix = ''
        self.link = ''
        self.playlist = options.playlist_id
        self.source = options.source_id
        self.user_id = options.user_id

    def json(self):
        return {'name':self.name, 'season':self.season, 'episode':self.episode, \
                'playlist_id':self.playlist, 'source_id':self.source, 'user_id':self.user_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, track_id):
        return cls.query.filter_by(id=track_id).first()
