from requests import get, post, delete
from flask import jsonify


# тестирование получения всех пользоателей
request1 = get('http://127.0.0.1:5000/api/v2/users')
print(request1.json())

# тестрование корректного получения одного пользователя
request2 = get('http://127.0.0.1:5000/api/v2/users/1')
print(request2.json())

# тестирование некорректного получения одного пользователя
request3 = get('http://127.0.0.1:5000/api/v2/users/1000000000')
print(request3.json())

# тестирование корректного добавления пользователя
user_data = jsonify({
                  'surname': 'test',
                  'name': 'test',
                  'age': 11,
                  'position': 'test',
                  'speciality': None,
                  'address': None,
                  'email': 'test',
                  'hashed_password': None,
                  'modified_date': None,
                  'jobs': None})
request4 = post('http://127.0.0.1:5000/api/v2/users', json=user_data)
print(request4.json())

# тестирование корректного удаления пользователя
request5 = delete('http://127.0.0.1:5000/api/v2/users/1')
print(request5.json())

# тестирование некорректного удаления пользователя
request6 = delete('http://127.0.0.1:5000/api/v2/users/10000000000000')
print(request5.json())
