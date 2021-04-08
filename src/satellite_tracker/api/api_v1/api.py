from fastapi import APIRouter

from satellite_tracker.api.api_v1.endpoints import index

api_router = APIRouter()
api_router.include_router(index.router, tags=["index"])
