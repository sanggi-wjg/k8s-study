from pydantic import BaseModel


class HealthResponseDto(BaseModel):
    status: str


class CacheResponseDto(BaseModel):
    key: str
    value: int


class CalculationResponseDto(BaseModel):
    result: int
