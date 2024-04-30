from fastapi import APIRouter, HTTPException
from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_session
from app.cruds import cars as service
from app.schemas.cars import CarSchema

router = APIRouter(
    tags=["Cars"],
    responses={404: {"description": "Not found"}},
)


@router.get("/car-info", status_code=200)
async def get_car_info(
        session: AsyncSession = Depends(get_session),
        model: str = None,
        year: int = None,
        body_type: str = None
):
    cars = await service.get_cars(session, model=model, year=year, body_type=body_type)
    if not cars:
        raise HTTPException(status_code=404, detail="Cars not found")
    return cars


@router.get("/car-info-{id}", status_code=200)
async def get_car_info(id: int, session: AsyncSession = Depends(get_session)):
    cars = await service.get_car(session, id)
    if not cars:
        raise HTTPException(status_code=404, detail="Cars not found")
    return cars


@router.post("/add-car", status_code=201)
async def add_car(car_data: CarSchema, session: AsyncSession = Depends(get_session)):
    await service.add_car(session, car_data)
    return {"message": "Car added successfully"}


@router.put("/edit-car-{id}", status_code=200)
async def add_car(id: int, car_data: CarSchema, session: AsyncSession = Depends(get_session)):
    await service.edit_car(session, car_data, id)
    return {"message": "Car edited successfully"}
