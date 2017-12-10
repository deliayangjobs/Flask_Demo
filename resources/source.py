from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.source import SourceModel


class Source(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('url',
        type=str
    )

    # @jwt_required()
    def get(self, source_id):
        source = SourceModel.find_by_id(source_id)
        if source:
            return source.json()
        return {'message':'Source not found'}, 404

    # @jwt_required()
    def post(self):
        data = Source.parser.parse_args()
        if SourceModel.find_by_name(data.name):
            return {'message':'An source with name "{}" already exists.'.format(data.name)}, 400

        source = SourceModel(data)

        try:
            source.save_to_db()
        except:
            return {"message":"An error occurred inserting the source."}, 500

        return source.json(), 201

    # @jwt_required()
    def delete(self, source_id):
        source = SourceModel.find_by_id(source_id)
        if source:
            source.delete_from_db()

        return {'message':'Source deleted'}

    # @jwt_required()
    def put(self, source_id):
        data = Source.parser.parse_args()
        source = SourceModel.find_by_id(source_id)

        if source is None:
            source = SourceModel(data)
        else:
            source.name = data['name']
            source.url = data['url']

        source.save_to_db()

        return source.json(), 201


class Sources(Resource):
    # @jwt_required()
    def get(self):
        return {'sources': [source.json() for source in SourceModel.query.all()]}
