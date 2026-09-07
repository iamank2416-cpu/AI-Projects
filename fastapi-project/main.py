from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"my first API is working"}

@app.get("/about")
def about():
    return {"project":"loan risk model", "version":"1.0"}