from pydantic import BaseModel


class HealthCheckData(BaseModel):
    status: str