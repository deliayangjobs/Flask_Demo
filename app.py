import os

from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister, Users
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.track import Track, Tracks
from resources.playlist import Playlist, Playlists
from resources.source import Source, Sources

app = Flask(__name__, template_folder='./views/templates')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# @app.before_first_request
# def create_tables():
#     db.create_all()

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(Track, '/track', '/track/<int:track_id>')
api.add_resource(Tracks, '/tracks')

api.add_resource(Playlist, '/playlist', '/playlist/<int:playlist_id>')
api.add_resource(Playlists, '/playlists')

api.add_resource(Source, '/source', '/source/<int:source_id>')
api.add_resource(Sources, '/sources')

api.add_resource(UserRegister, '/register', '/profile/<int:user_id>')
api.add_resource(Users, '/users')


@app.route('/')
def index():
    tv_show="The Office"
    return render_template("index.html", show=tv_show)


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
