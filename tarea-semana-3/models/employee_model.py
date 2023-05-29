from sqlalchemy.schema import Column
from sqlalchemy import types
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from db import conexion

class EmployeeModel(conexion.Model):
    __tablename__='employees'
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    name = Column(type_=types.Text, nullable=False)
    lastName = Column(type_=types.Text, name="last_name", nullable=False)
    email = Column(type_=types.Text, nullable=False, unique=True)
    areaId = Column(ForeignKey(column='areas.id'),name="area_id", nullable=False, type_=types.Integer)

    area = relationship("AreaModel", back_populates="employees")