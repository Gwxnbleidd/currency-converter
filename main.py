from fastapi import FastAPI
import uvicorn
from app.api.endpoints.auth import auth_rout
from app.api.endpoints.endpoints import currencies_router
from app.database.orm import create_tables
app = FastAPI()

app.include_router(auth_rout)
app.include_router(currencies_router)

if __name__ == '__main__':

    # create_tables()
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)