"""Health Check."""

from fastapi import APIRouter, Depends

router = APIRouter(prefix="/health-check", tags=["Health Check"])


@router.get('')
async def health_check():
    return {'messsage': 'all is ok'}

