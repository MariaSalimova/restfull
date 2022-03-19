from requests import get, post
from datetime import datetime


from datetime import datetime

import requests


def post_jobs(json):
    post_response = requests.post("http://127.0.0.1:5000/api/jobs", json=json)
    data = post_response.json()
    if "success" in data:
        print("Добавлен")
    else:
        print("Ошибка:", data["error"])


# ok
job_data1 = {"id": 5,
             "job": 'job 1',
             "work_size": 23,
             "collaborators": '1, 2',
             "end_date": datetime.now(),
             "start_date": datetime.now(),
             "is_finished": False,
             "team_leader": 1
             }

# id already exists
job_data2 = {"id": 5,
             "job": 'job 1',
             "work_size": 23,
             "collaborators": '1, 2',
             "end_date": None,
             "start_date": datetime.now(),
             "is_finished": False,
             "team_leader": 1
             }

# Bad request (не все поля)
job_data3 = {"id": 6,
             "job": 'job 1',
             "work_size": 23,
             "collaborators": '1, 2',
             "is_finished": False,
             "team_leader": 1
             }

# Empty request
job_data4 = {}


get_response = requests.get("http://127.0.0.1:5000/api/jobs")
jobs_length = len(get_response.json()["jobs"])
print(f"Количество работ: {jobs_length}")


# ok
post_jobs(job_data1)
# id already exists
post_jobs(job_data2)
# Bad request (не все поля)
post_jobs(job_data3)
# Empty request
post_jobs(job_data4)
get_response = requests.get("http://127.0.0.1:5000/api/jobs")
jobs_length = len(get_response.json()["jobs"])
print(f"Количество работ: {jobs_length}")

