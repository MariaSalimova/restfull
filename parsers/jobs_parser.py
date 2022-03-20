from flask_restful import reqparse

jobs_parser = reqparse.RequestParser()
jobs_parser.add_argument('team_leader')
jobs_parser.add_argument('job')
jobs_parser.add_argument('work_size')
jobs_parser.add_argument('collaborators')
jobs_parser.add_argument('start_date')
jobs_parser.add_argument('end_date')
jobs_parser.add_argument('is_finished')
jobs_parser.add_argument('leader')
