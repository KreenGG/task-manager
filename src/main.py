from contextlib import asynccontextmanager
import logging
from typing import AsyncGenerator
from fastapi import FastAPI
from src.config import settings


uvicorn_logger = logging.getLogger('uvicorn.error')
uvicorn_logger.level = logging.DEBUG
@asynccontextmanager
async def lifespan(_application: FastAPI) -> AsyncGenerator:
    # Startup
    uvicorn_logger.info("App startup (lifespan)")
    uvicorn_logger.debug(settings.DATABASE_URL)
    yield
    # Shutdown
    uvicorn_logger.info("App shutdown (lifespan)")

app = FastAPI(
    docs_url="/api/docs",
    lifespan=lifespan,
    )

@app.get("/healthcheck")
async def healthcheck() -> dict[str, bool]:
    return {"status": True}
