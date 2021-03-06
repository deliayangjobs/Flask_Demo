from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.track import TrackModel


class Track(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('season',
        type=int
    )
    parser.add_argument('episode',
        type=int
    )
    parser.add_argument('playlist_id',
        type=int
    )
    parser.add_argument('source_id',
        type=int
    )
    parser.add_argument('user_id',
        type=int
    )

    # @jwt_required()
    def get(self, track_id):
        track = TrackModel.find_by_id(track_id)
        if track:
            return track.json()
        return {'message':'Source not found'}, 404

    def post(self):
        data = Track.parser.parse_args()
        if TrackModel.find_by_name(data.name):
            return {'message':'An track with name "{}" already exists.'.format(data.name)}, 400

        track = TrackModel(data)

        try:
            track.save_to_db()
        except:
            return {"message":"An error occurred inserting the track."}, 500

        return track.json(), 201
    #
    # def delete(self, name):
    #     item = ItemModel.find_by_name(name)
    #     if item:
    #         item.delete_from_db()
    #
    #     return {'message':'item deleted'}
    #
    # def put(self, name):
    #     data = Item.parser.parse_args()
    #     # data = request.get_json()
    #     item = ItemModel.find_by_name(name)
    #
    #     if item is None:
    #         # try:
    #             # new_item.insert()
    #             # ItemModel.insert(new_item)
    #         # except:
    #             # return {"message":"An error occurred inserting the item."}, 500
    #         item = ItemModel(name, **data)
    #     else:
    #         # try:
    #         #     new_item.update() #little weird here, but this is the itemModel with new price
    #             # ItemModel.update(new_item)
    #         # except:
    #         #     return {"message":"An error occurred updating the item."}, 500
    #         item.price = data['price']
    #
    #     item.save_to_db()
    #
    #     return item.json(), 201


class Tracks(Resource):
    # @jwt_required()
    def get(self):
        return {'tracks': [track.json() for track in TrackModel.query.all()]}
