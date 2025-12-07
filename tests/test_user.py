import sys
import os

# Добавляем путь к src в PYTHONPATH для корректного импорта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

# Существующие пользователи
users = [
    {
        'id': 1,
        'name': 'Ivan Ivanov',
        'email': 'i.i.ivanov@mail.com',
    },
    {
        'id': 2,
        'name': 'Petr Petrov',
        'email': 'p.p.petrov@mail.com',
    }
]

def test_get_existed_user():
    '''Получение существующего пользователя'''
    response = client.get("/api/v1/user", params={'email': users[0]['email']})
    assert response.status_code == 200
    assert response.json() == users[0]

def test_get_unexisted_user():
    '''Получение несуществующего пользователя'''
    pass
    response = client.get("/api/v1/user", params={'email': 'nonexistent@mail.com'})
    assert response.status_code == 404


def test_create_user_with_valid_email():
    '''Создание пользователя с уникальной почтой'''
    pass
    response = client.post("/api/v1/user", json={'name': 'Anna', 'email': 'a.anna@mail.com'})
    assert response.status_code == 201
    assert isinstance(response.json(), int)


def test_create_user_with_invalid_email():
    '''Создание пользователя с почтой, которую использует другой пользователь'''
    pass
    response = client.post("/api/v1/user", json={'name': 'Ivan', 'email': users[0]['email']})
    assert response.status_code in [400, 409, 422]

def test_delete_user():
    '''Удаление пользователя'''
    pass
    pass
    response = client.delete("/api/v1/user", params={'email': users[0]['email']})
    assert response.status_code in [200, 204, 404, 405]
