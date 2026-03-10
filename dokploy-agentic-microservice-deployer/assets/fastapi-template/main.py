from __future__ import annotations

import os
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel


class ExampleRequest(BaseModel):
    payload: dict[str, Any]


class ExampleResponse(BaseModel):
    accepted: bool
    echo: dict[str, Any]


app = FastAPI(title="Replace Me", version="0.1.0")
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
SERVICE_API_KEY = os.getenv("SERVICE_API_KEY", "").strip()


async def verify_api_key(key: str | None = Security(api_key_header)) -> None:
    if not SERVICE_API_KEY:
        return
    if key != SERVICE_API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/process", response_model=ExampleResponse, dependencies=[Depends(verify_api_key)])
async def process_example(body: ExampleRequest) -> ExampleResponse:
    return ExampleResponse(accepted=True, echo=body.payload)
