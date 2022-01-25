from uvicorn import run

from api.main import create_app

app = create_app()

if __name__ == "__main__":
    run("api.main:app", host="127.0.0.1", port=8000)