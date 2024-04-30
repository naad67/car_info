from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.car import Car


async def get_cars(session: AsyncSession, **kwargs):
    query = select(Car)
    if kwargs.get('model'):
        query = query.filter(func.concat(Car.make, ' ', Car.model).like(f'%{kwargs["model"]}%'))

    if kwargs.get('year'):
        query = query.filter(Car.year == kwargs["year"])

    if kwargs.get('body_type'):
        query = query.filter(Car.body_type == kwargs["body_type"])

    result = await session.execute(query)
    return result.scalars().all()


async def get_car(session: AsyncSession, id: int):
    async with session.begin():
        car = await session.get(Car, id)
        if car is None:
            raise HTTPException(status_code=404, detail=f"Car with id {id} not found")
        return car


async def add_car(session: AsyncSession, car_data: Car):
    async with session.begin():
        session.add(Car(**car_data.dict()))


async def edit_car(session: AsyncSession, car_data: Car, id: int):
    async with session.begin():
        car = await session.get(Car, id)
        if car is None:
            raise HTTPException(status_code=404, detail=f"Car with id {id} not found")

        for field, value in car_data.dict().items():
            setattr(car, field, value)
