from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from app.core.config import settings
import csv
from app.models.car import Car
import asyncio

engine = create_async_engine(settings.database_url, echo=True)

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def insert_data_from_csv():
    async with async_session() as session:
        with open('data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['engine_volume'])
                car = Car(
                    make=row['make'],
                    model=row['model'],
                    year=int(row['year']),
                    body_type=row['body_type'],
                    engine_volume=float(row['engine_volume']),
                    power=int(row['power'])
                )

                session.add(car)

            await session.commit()


async def main():
    await insert_data_from_csv()

asyncio.run(main())