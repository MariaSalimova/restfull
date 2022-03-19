from data import db_session
from flask import Flask, render_template, redirect, request, abort, make_response, jsonify
from routs import jobs_blueprint
from flask_restful import reqparse, abort, Api, Resource
from resorces import UsersResource, UsersListResource

app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    db_session.global_init('database.db')
    app.register_blueprint(jobs_blueprint)
    api.add_resource(UsersResource, '/api/v2/users/<int:user_id>')
    api.add_resource(UsersListResource, '/api/v2/users')
    app.run()


if __name__ == '__main__':
    main()
