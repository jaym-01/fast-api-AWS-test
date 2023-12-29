from fastapi import FastAPI
from src.models.root_models import AddBody

app = FastAPI()

@app.post("/add")
async def post_add(jsonBody: AddBody):
    ans = jsonBody.x + jsonBody.y

    return {"ans": ans}

@app.get("/")
async def get_root():
    return "hello this is a test from the docker container!!"