from fastapi import FastAPI

app = FastAPI()


@app.get('/info')
async def get_info():
    return "a FastApi based application for you eng practise"