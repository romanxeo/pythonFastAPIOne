from fastapi import FastAPI
from db.base import database
from endpoints import users, auth
import uvicorn

app = FastAPI(title="test FastAPI")
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get('/')
async def index():
    return {'message': "hello"}

@app.get('/greet/{name}')
def greet_name(name:str):
    return {'messager': f"hello {name}"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)
