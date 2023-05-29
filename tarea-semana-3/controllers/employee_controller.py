from flask_restful import Resource
from db import conexion
from models.employee_model import EmployeeModel

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
        try:
            conexion.session.commit()
            return {
                'message': 'Usuario creado exitosamente'
            }, 201
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Erro al crear el empleado',
                'content': error.args
            }, 400