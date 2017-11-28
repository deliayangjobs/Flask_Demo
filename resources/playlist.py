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
    # def get(self, name):
    #     item = ItemModel.find_by_name(name)
    #     if item:
    #         return item.json()
    #     return {'message':'Item not found'}, 404

    def post(self, playlist_id):
        # if ItemModel.find_by_name(name):
        #     return {'message':'An item with name "{}" already exists.'.format(name)}, 400

        data = Playlist.parser.parse_args()
        # data = request.get_json()
        # item = ItemModel(name, data['price'], data['store_id'])
        # track = TrackModel(track_id, **data)
        playlist = PlaylistModel(playlist_id, data)

        try:
            playlist.save_to_db()
        except:
            return {"message":"An error occurred inserting the playlist."}, 500

        return playlist.json(), 201