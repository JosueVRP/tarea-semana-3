from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.employee_model import EmployeeModel


class EmployeeResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model = EmployeeModel

class EmployeeRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = EmployeeModel
        include_fk = True