from fastapi import APIRouter, Depends, HTTPException,status

from app.utilits.external_api import (get_list_of_currencies, get_actual_convert_currencies, 
                                      convert_currencies)

from app.api.endpoints.auth import get_user_from_token
from app.api.shemas import (AnswerConvertCurrencies, AnswerListCurrencies,
                            AnswerActualCurrencies)

currencies_router = APIRouter(prefix='/currencies')

@currencies_router.get('/list')
def app_get_and_pocess_list_of_currencies(user = Depends(get_user_from_token)):
    res = get_list_of_currencies()
    answer = AnswerListCurrencies(answer=res['symbols'])
    return answer

@currencies_router.post('/get_actual_currencies')
def app_get_actual_currencies(base = None, symbols = None, user = Depends(get_user_from_token)):
    try:
        res = get_actual_convert_currencies(base, symbols)
        answer = AnswerActualCurrencies(base= res['base'],
                                        date=res['date'],
                                        rates=res['rates'])
        return answer
    except:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                             detail='Incorrect input data (Symbols must be separated by commas)')

@currencies_router.post('/convert_currencies')
def app_convert_currencies(_from, to, amount, user = Depends(get_user_from_token)):
    try:
        res = convert_currencies(_from, to, amount)
        return AnswerConvertCurrencies(input_data= res['query'],
                                    result = res['result'],
                                    rate=res['info']['rate'])
    except:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Incorrect input data')