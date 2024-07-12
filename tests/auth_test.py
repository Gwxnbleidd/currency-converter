from fastapi.testclient import TestClient

import sys
sys.path.append('/home/dmitry/Учеба/FastAPI проекты/Конвертатор валют')
from main import app

client = TestClient(app)

def test_register_and_login():
    # user_data = {'username': 'Vika',
    #         'password':'6789',
    #         'email': 'vika@mail.ru'}
    
    # response = client.post(url='/auth/register', json=user_data)

    # assert response.status_code==200
    # assert response.json() == {'Welcome, Vika'}

    user_data = {'username': 'Dima',
            'password':'1234'}    
    response = client.post(url='/auth/login', json=user_data)

    assert response.status_code==200
    assert response.json() == {'message':'Successfull'}

    user_data = {'username': 'Dima',
            'password':'1234',
            'email': 'dima@example.com'}
    
    response = client.post(url='/auth/register', json=user_data)

    assert response.status_code==409
    assert response.json() == {'A user with the same name already exists!'}

    user_data = {'username': 'Dima',
            'password':'134'}    
    response = client.post(url='/auth/login', json=user_data)

    assert response.status_code==401
    assert response.json() == {'Incorrect password!'}

    user_data = {'username': 'Dsma',
            'password':'1234'}    
    response = client.post(url='/auth/login', json=user_data)

    assert response.status_code==404
    assert response.json() == {'User not found'}


