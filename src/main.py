import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.v1 import router as router_v1
from configs.config import settings
from configs.logger import logger


app = FastAPI(name="Shortcut API v.0.1")

app.include_router(router_v1, prefix="")


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred."},
    )


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.SERVICE_PORT,
    )
