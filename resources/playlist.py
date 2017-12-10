from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.playlist import PlaylistModel


class Playlist(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('description',
        type=str
    )

    # @jwt_required()
    def get(self, playlist_id):
        playlist = PlaylistModel.find_by_id(playlist_id)
        if playlist:
            return playlist.json()
        return {'message':'Playlist not found'}, 404

    # @jwt_required()
    def post(self):
        data = Playlist.parser.parse_args()
        if PlaylistModel.find_by_name(data.name):
            return {'message':'An playlist with name "{}" already exists.'.format(data.name)}, 400

        playlist = PlaylistModel(data)

        try:
            playlist.save_to_db()
        except:
            return {"message":"An error occurred inserting the playlist."}, 500

        return playlist.json(), 201

    # @jwt_required()
    def delete(self, playlist_id):
        playlist = PlaylistModel.find_by_id(playlist_id)
        if playlist:
            playlist.delete_from_db()

        return {'message':'Playlist deleted'}

    # @jwt_required()
    def put(self, playlist_id):
        data = Playlist.parser.parse_args()
        playlist = PlaylistModel.find_by_id(playlist_id)

        if playlist is None:
            playlist = PlaylistModel(data)
        else:
            playlist.name = data['name']
            playlist.description = data['description']

        playlist.save_to_db()

        return playlist.json(), 201


class Playlists(Resource):
    # @jwt_required()
    def get(self):
        return {'playlists': [playlist.json() for playlist in PlaylistModel.query.all()]}
