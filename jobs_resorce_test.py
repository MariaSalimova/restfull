from requests import get, post, delete
from flask import jsonify

# корректное получение всех работ
request1 = get('http://127.0.0.1:5000/api/v2/jobs')
print(request1.json())

# корректное получение одной работы
request2 = get('http://127.0.0.1:5000/api/v2/jobs/1')
print(request2.json())

# некорректное получение одной работы
request3 = get('http://127.0.0.1:5000/api/v2/jobs/1000000000000000000')
print(request3.json())

# корректное добавление работы
job_data = jsonify({'team_leader': None,
                    'job': 'test',
                    'work_size': 1,
                    'collaborators': None,
                    'end_date': None,
                    'is_finished': False,
                    'leader': 1})
request4 = post('http://127.0.0.1:5000/api/v2/jobs', json=job_data)
print(request4.json())

# корректное удаление работы
request5 = delete('http://127.0.0.1:5000/api/v2/jobs/1')
print(request5.json())

# некорректное удаление работы
request6 = delete('http://127.0.0.1:5000/api/v2/jobs/10000000000000')
print(request5.json())
