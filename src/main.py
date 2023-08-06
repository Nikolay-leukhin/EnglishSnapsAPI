from fastapi import FastAPI
from src.routers import user_router, ssn_router, msg_router
from src.routers.theme import router as theme_router


app = FastAPI()

app.include_router(user_router)
app.include_router(ssn_router)
app.include_router(msg_router)
app.include_router(theme_router)



@app.get('/')
async def get_info():
    return "ping succes"

