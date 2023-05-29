from flask_restful import Resource,request
from db import conexion
from models.area_model import AreaModel
from dtos.area_dto import AreaRequestDto, AreaResponseDto

class AreaController(Resource):
    def get(self):
        result = conexion.session.query(AreaModel).all()
        dto = AreaResponseDto(many=True)
        data = dto.dump(result)
        return {
            'content': data
        }
    
    def get(self, id):
        area = conexion.session.query(AreaModel).get(id)

        if area:
            dto = AreaResponseDto()
            data = dto.dump(area)
            return {
                'content': data
            }
        else:
            return {
                'message': 'El área no existe'
            }, 404


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