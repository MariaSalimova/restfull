from flask_restful import Resource, abort
from data.jobs import Jobs
from data import db_session
from flask import jsonify
from parsers import jobs_parser


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    @staticmethod
    def get(job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(
            only=('id',
                  'team_leader',
                  'job',
                  'work_size',
                  'collaborators',
                  'start_date',
                  'end_date',
                  'is_finished',
                  'leader'))})

    @staticmethod
    def delete(job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    @staticmethod
    def get():
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id',
                  'team_leader',
                  'job',
                  'work_size',
                  'collaborators',
                  'start_date',
                  'end_date',
                  'is_finished',
                  'leader')) for item in jobs]})

    @staticmethod
    def post():
        args = jobs_parser.parse_args()
        session = db_session.create_session()
        job = Jobs(**args)
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
