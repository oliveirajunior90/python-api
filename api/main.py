from fastapi import FastAPI

from api.routers.views import RouterViews

app: FastAPI = FastAPI(
    title="API",
    description="Api backend API",
)


def create_app():
    RouterViews(app)
    return app