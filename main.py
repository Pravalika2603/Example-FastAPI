from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return "Pravalika"

@app.get("/2")
def read_root():
    return "P"