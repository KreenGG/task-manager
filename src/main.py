from contextlib import asynccontextmanager
import logging
from typing import AsyncGenerator
from fastapi import FastAPI


uvicorn_logger = logging.getLogger('uvicorn.error')
@asynccontextmanager
async def lifespan(_application: FastAPI) -> AsyncGenerator:
    # Startup
    uvicorn_logger.info("App startup (lifespan)")
    yield
    # Shutdown
    uvicorn_logger.info("App shutdown (lifespan)")

app = FastAPI(lifespan=lifespan)


@app.get("/healthcheck")
async def healthcheck() -> dict[str, bool]:
    return {"status": True}
