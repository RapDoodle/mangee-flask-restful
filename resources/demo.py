from flask_restful import Resource, reqparse
from models.demo import DemoModel
from flask_jwt import jwt_required
from flask import current_app


class Demo(Resource):
    add_parser = reqparse.RequestParser()
    add_parser.add_argument('value',
                        type=str,
                        required=True,
                        help='The value of the object cannot be empty.'
                        )

    get_parser = reqparse.RequestParser()
    get_parser.add_argument('id',
                        type=int,
                        required=False
                        )
    get_parser.add_argument('value',
                        type=str,
                        required=False
                        )

    @jwt_required()
    def post(self):
        data = Demo.add_parser.parse_args()

        demo_obj = DemoModel(data['value'])
        demo_obj.save()

        return {'message': 'Object added successfully.'}, 201

    def get(self):
        data = Demo.get_parser.parse_args()

        res = DemoModel.search(_id=data['id'], value=data['value'])
        if res and len(res[0]) > 0:
            jsoned = [obj.json() for obj in res[0]]
            return {'result': jsoned}, 200
        
        return '', 204

    @jwt_required()
    def delete(self):
        data = Demo.get_parser.parse_args()
        
        res = DemoModel.find_by_id(_id=data['id'])
        if res is not None and isinstance(res, DemoModel):
            res.delete()
            return {'message': 'Deleted successfully.'}, 200

        return {'message': 'Object not found.'}, 200
