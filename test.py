from requests import get
from flask import make_response, jsonify


# получение всех работ
print(get('http://127.0.0.1:5000/api/jobs'))

# корректное получение одной работы
print(get('http://127.0.0.1:5000/api/jobs/1'))

# Ошибочный запрос на получение одной работы — неверный id
print(get('http://127.0.0.1:5000/api/jobs/10000000000000000'))

# Ошибочный запрос на получение одной работы — строка
print(get('http://127.0.0.1:5000/api/jobs/id'))
