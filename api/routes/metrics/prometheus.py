"""Prometheus Metrics."""

from fastapi import APIRouter

router = APIRouter(prefix="/prometheus", tags=["Prometheus Metrics"])


@router.get('/metrics')
async def health_check():
    return {'messsage': 'all is ok'}

