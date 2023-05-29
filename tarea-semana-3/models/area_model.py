from sqlalchemy.schema import Column
from sqlalchemy import types
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from db import conexion

class AreaModel(conexion.Model):
    __tablename__ = 'areas'
    id = Column(type_=types.Integer, autoincrement=True,primary_key=True)
    name = Column(type_=types.Text, nullable=False)
    floor = Column(type_=types.Integer)

    employees = relationship("EmployeeModel", back_populates="area")