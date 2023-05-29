from flask_restful import Resource
from db import conexion
from models.area_model import AreaModel

class AreaController(Resource):
    def get(self):
        result = conexion.session.query(AreaModel).all()
        dto = AreaResponseDto(many=True)
        data = dto.dump(result)
        return {
            'content': data
        }


    def post(self):
        data = request.json
        dto = AreaRequestDto()
        dataValidate = dto.load(data)
        print(dataValidate)
        newArea = AreaModel(**dataValidate)
        conexion.session.add(newArea)
        try:
            conexion.session.commit()
            return {
                'message': 'Area creada exitosamente'
            }, 201
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Erro al crear el Area',
                'content': error.args
            }, 400