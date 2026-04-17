from fastapi import APIRouter

from app.schemas.common import SuccessResponse
from app.schemas.health import HealthCheckData

router = APIRouter()


@router.get("", response_model=SuccessResponse[HealthCheckData], summary="Health check")
async def health_check() -> SuccessResponse[HealthCheckData]:
    return SuccessResponse(data=HealthCheckData(status="ok"))