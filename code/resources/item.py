import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message':'An item with name "{}" already exists.'.format(name)}, 400

        data = Item.parser.parse_args()
        # data = request.get_json()
        item = ItemModel(name, data['price'])

        try:
            item.save_to_db()
        except:
            return {"message":"An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message':'item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        # data = request.get_json()
        item = ItemModel.find_by_name(name)

        if item is None:
            # try:
                # new_item.insert()
                # ItemModel.insert(new_item)
            # except:
                # return {"message":"An error occurred inserting the item."}, 500
            item = ItemModel(name, data['price'])
        else:
            # try:
            #     new_item.update() #little weird here, but this is the itemModel with new price
                # ItemModel.update(new_item)
            # except:
            #     return {"message":"An error occurred updating the item."}, 500
            item.price = data['price']

        item.save_to_db()

        return item.json(), 201


class ItemList(Resource):
    def get(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append(ItemModel(row[1], row[2]).json())

        conn.close()
        return {'items':items}
