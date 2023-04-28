from fastapi import FastAPI
from routers import router as user_router

app = FastAPI()

app.include_router(user_router)


@app.get('/info')
async def get_info():
    return "a FastApi based application for you eng practise"