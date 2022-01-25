from fastapi import FastAPI

from api.routers.views import RouterViews

app: FastAPI = FastAPI(
    title="API",
    description="Api backend API",
)
"""
database = [
    User(id=1, email="roger@roger.com.br", password="roger123"),
    User(id=2, email="waters@waters.com.br", password="waters123"),
]
"""
def create_app():
    RouterViews(app)
    return app