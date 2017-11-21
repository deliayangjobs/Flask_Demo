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
    # parser.add_argument('store_id',
    #     type=int,
    #     required=True,
    #     help="Every item needs a store id."
    # )
    #
    # @jwt_required()
    # def get(self, name):
    #     item = ItemModel.find_by_name(name)
    #     if item:
    #         return item.json()
    #     return {'message':'Item not found'}, 404

    def post(self, track_id):
        # if ItemModel.find_by_name(name):
        #     return {'message':'An item with name "{}" already exists.'.format(name)}, 400

        data = Track.parser.parse_args()
        # data = request.get_json()
        # item = ItemModel(name, data['price'], data['store_id'])
        # track = TrackModel(track_id, **data)
        track = TrackModel(track_id, data)

        try:
            track.save_to_db()
        except:
            return {"message":"An error occurred inserting the item."}, 500

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


# class ItemList(Resource):
#     def get(self):
#         return {'items': [item.json() for item in ItemModel.query.all()]}
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
