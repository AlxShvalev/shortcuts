import uvicorn
from fastapi import FastAPI

from api.v1 import router as router_v1
from configs.config import settings


app = FastAPI(name="Shortcut API v.0.1")

app.include_router(router_v1, prefix="")


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.SERVICE_PORT,
        reload=settings.DEBUG,
    )
