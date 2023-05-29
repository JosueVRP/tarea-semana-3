from flask_restful import Resource, request
from db import conexion
from models.employee_model import EmployeeModel
from dtos.employee_dto import EmployeeResponseDto, EmployeeRequestDto

class EmployeeController(Resource):
    def get(self):
        result = conexion.session.query(EmployeeModel).all()
        dto = EmployeeResponseDto(many=True)
        data = dto.dump(result)
        return {
            'content': data
        }

    def post(self):
        data = request.json
        dto = EmployeeRequestDto()
        dataValidate = dto.load(data)
        print(dataValidate)

        newEmployee = EmployeeModel(**dataValidate)
        conexion.session.add(newEmployee)
        conexion.session.commit()
        
        try:
            return {
                'message': 'Usuario creado exitosamente'
            }, 201
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Error al crear el empleado',
                'content': error.args
            }, 400
