import math
import random

import uvicorn
from fastapi import FastAPI, Depends
from fastapi_healthchecks.api.router import HealthcheckRouter, Probe
from fastapi_healthchecks.checks.http import HttpCheck
from fastapi_healthchecks.checks.redis import RedisCheck
from fastapi_healthchecks.checks.settings import SettingsCheck
from starlette import status

from src.config import get_settings, Settings
from src.dto import CacheResponseDto, HealthResponseDto, CalculationResponseDto
from src.redis_client import RedisClient, get_redis_client

app = FastAPI()
config = get_settings()

app.include_router(
    HealthcheckRouter(
        Probe(
            name="liveness",
            checks=[
                HttpCheck(url="http://127.0.0.1:8000/health", timeout=5.0),
                SettingsCheck(name="Settings", settings_class=Settings),
                RedisCheck(
                    host=config.REDIS_HOST,
                    port=config.REDIS_PORT,
                    db=config.REDIS_DB,
                    timeout=10.0,
                ),
            ],
        ),
        Probe(
            name="readiness",
            checks=[
                HttpCheck(url="http://127.0.0.1:8000/cache", timeout=5.0),
            ],
        ),
    ),
)


@app.get(
    "/health",
    summary="Health",
    status_code=status.HTTP_200_OK,
)
async def health() -> HealthResponseDto:
    return HealthResponseDto(status="OK")


@app.get(
    "/",
    summary="Root",
    status_code=status.HTTP_200_OK,
)
async def root() -> str:
    return "Hello World"


@app.get(
    path="/factorial",
    summary="Simple factorial",
    status_code=status.HTTP_200_OK,
)
async def simple_calc() -> CalculationResponseDto:
    rand = random.randint(1, 100)
    return CalculationResponseDto(result=math.factorial(rand))


@app.get(
    "/cache",
    summary="Simple cache hit miss",
    status_code=status.HTTP_200_OK,
)
async def simple_cache(
    redis_client: RedisClient = Depends(get_redis_client),
) -> CacheResponseDto:
    rand = random.randint(1, 100)
    key = f"simple-key:{rand}"
    return CacheResponseDto(
        key=key,
        value=redis_client.get_or_set(key, rand, 60),
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        reload_delay=1,
        use_colors=True,
    )
