from fastapi.testclient import TestClient

import sys
import os
sys.path.append('/home/dmitry/Учеба/FastAPI проекты/Конвертатор валют/')
from main import app

client = TestClient(app)

# def test_register():
    
#     user_data = {
#         'username': 'Vika',
#         'password': '678910',
#         'email': 'kavi@mail.ru',
#         'active': True
#         }
    
# #     response = client.post(url='/auth/register?username=Vika&password=4567&email=ya%40ya.ru&active=true')

# #     assert response.status_code == 200
# #     assert response.json() == ['Welcome, Vika']

#     user_data = {'username': 'Dima',
#             'password':'1234',
#             'email': 'dima@example.com'}
    
#     response = client.post(url=f'/auth/register', json = user_data)

#     assert response.status_code==409
#     assert response.json() == ['A user with the same name already exists!']





def test_login():

    user_data = {'username': 'Dima',
                'password':'1234'}   
     
    response = client.post(url='/auth/login', data = user_data)

    assert response.status_code==200
    assert response.json() == {'message':'Successfull!'}

    user_data = {'username': 'Dsma',
                'password':'1234'}    
    
    response = client.post(url='/auth/login', data=user_data)

    assert response.status_code==404
    assert response.json() == {'detail': 'User not found'}

        
    user_data = {'username': 'Dima',
            'password':'134'}    
    
    response = client.post(url='/auth/login', data=user_data)

    assert response.status_code==401
    assert response.json() == {'detail':'Incorrect password!'}


