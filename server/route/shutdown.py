import os
from fastapi import APIRouter

shutdown_route = APIRouter()

@shutdown_route.get("/shutdown")
async def shutdown():
    os._exit(0)