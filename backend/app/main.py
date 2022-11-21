from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .routers import groups, users


def api() -> FastAPI:
    app = api_factory(title="FastAPI", allow_origins=["http://localhost:5000"])

    return app


def api_factory(title: str, allow_origins: list[str] = ["http://localhost:5000"]) -> FastAPI:

    app = FastAPI(title=title)
    app.include_router(router=groups.router)
    app.include_router(router=users.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.mount("/static", StaticFiles(directory="static"), name="static")

    return app
