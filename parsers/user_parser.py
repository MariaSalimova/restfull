from flask_restful import reqparse

user_parser = reqparse.RequestParser()
user_parser.add_argument('surname', required=True)
user_parser.add_argument('name', required=True)
user_parser.add_argument('age')
user_parser.add_argument('position')
user_parser.add_argument('speciality')
user_parser.add_argument('address')
user_parser.add_argument('email', required=True)
user_parser.add_argument('hashed_password')
user_parser.add_argument('modified_date')
user_parser.add_argument('jobs')
