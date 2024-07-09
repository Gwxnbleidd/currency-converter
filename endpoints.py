from fastapi import APIRouter, Depends

from app.utilits.external_api import (get_list_of_currencies,process_list_of_currencies, 
                                      get_actual_convert_currencies, convert_currencies,process_convert_currencies)

from app.api.endpoints.auth import get_user_from_token

currencies_router = APIRouter(prefix='/currencies')

@currencies_router.get('/list')
def app_get_and_pocess_list_of_currencies(user = Depends(get_user_from_token)):
    print(user)
    res = get_list_of_currencies()
    return process_list_of_currencies(res)

@currencies_router.post('/get_actual_currencies')
def app_get_actual_currencies(base = None, symbols = None, user = Depends(get_user_from_token)):
    res = get_actual_convert_currencies(base, symbols)
    return res

@currencies_router.post('/convert_currencies')
def app_convert_currencies(_from, to, amount, user = Depends(get_user_from_token)):
    res = convert_currencies(_from, to, amount)
    return process_convert_currencies(res)

#Добавить модель ответа