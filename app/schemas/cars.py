from pydantic.main import BaseModel


class CarSchema(BaseModel):
    make: str
    model: str
    year: int
    body_type: str
    engine_volume: float
    power: int
