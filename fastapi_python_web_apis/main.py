# by Richi Rod AKA @richionline / falken20
# fastapi_python_web_apis/main.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!"}
