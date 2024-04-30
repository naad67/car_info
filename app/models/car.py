import sqlalchemy
from app.core.db import Base


class Car(Base):
    __tablename__ = 'cars'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    make = sqlalchemy.Column(sqlalchemy.String(20))
    model = sqlalchemy.Column(sqlalchemy.String(20))
    year = sqlalchemy.Column(sqlalchemy.Integer)
    body_type = sqlalchemy.Column(sqlalchemy.String(20))
    engine_volume = sqlalchemy.Column(sqlalchemy.Float)
    power = sqlalchemy.Column(sqlalchemy.Integer)