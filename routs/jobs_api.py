import flask
from data.jobs import Jobs
from data.db_session import global_init, create_session
from flask import jsonify, request


blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = create_session()
    jobs = db_sess.query(Jobs).all()
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id',
                                    'team_leader',
                                    'job',
                                    'work_size',
                                    'collaborators',
                                    'start_date',
                                    'end_date',
                                    'is_finished',
                                    'leader'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    db_sess = create_session()

    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'job':
                job.to_dict(only=('id',
                                  'team_leader',
                                  'job',
                                  'work_size',
                                  'collaborators',
                                  'start_date',
                                  'end_date',
                                  'is_finished',
                                  'leader'))

        }
    )


@blueprint.route('/', methods=['POST'])
def create_jobs():
    keys = ("id",
            "job",
            "work_size",
            "collaborators",
            "end_date",
            "start_date",
            "is_finished",
            "team_leader")
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in keys):
        return jsonify({'error': 'Bad request'})
    db_sess = create_session()
    exist_job = db_sess.query(Jobs).get(request.json["id"])
    if exist_job:
        return jsonify({'error': 'Id already exists'})
    data = {key: request.json[key] for key in keys}
    # print(data)
    jobs = Jobs(**data)
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})