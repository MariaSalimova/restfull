from flask_restful import Resource, abort
from data.user import User
from data import db_session
from flask import jsonify
from parsers import user_parser


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    @staticmethod
    def get(user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('id',
                  'surname',
                  'name',
                  'age',
                  'position',
                  'speciality',
                  'address',
                  'email',
                  'hashed_password',
                  'modified_date',
                  'jobs'))})

    @staticmethod
    def delete(user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    @staticmethod
    def get():
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id',
                  'surname',
                  'name',
                  'age',
                  'position',
                  'speciality',
                  'address',
                  'email',
                  'hashed_password',
                  'modified_date',
                  'jobs')) for item in users]})

    @staticmethod
    def post():
        args = user_parser.parse_args()
        session = db_session.create_session()
        user = User(**args)
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
