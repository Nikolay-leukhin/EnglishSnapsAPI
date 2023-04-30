from fastapi import FastAPI
from src.routers import user_router, ssn_router, msg_router


app = FastAPI()

app.include_router(user_router)
app.include_router(ssn_router)
app.include_router(msg_router)



@app.get('/info')
async def get_info():
    return "a FastApi based application for you eng practise"

