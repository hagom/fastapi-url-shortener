# shortener_app/main.py

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Bienvenido a la API para acortar URL"
