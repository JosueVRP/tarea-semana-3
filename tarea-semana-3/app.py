from flask import Flask
from db import conexion
from flask_migrate import Migrate
from models.area_model import AreaModel
from models.employee_model import EmployeeModel
from controllers.area_controller import AreaController
from controllers.employee_controller import EmployeeController
from flask_restful import Api

app = Flask(__name__)
api = Api(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/tarea3'

conexion.init_app(app)

Migrate(app,conexion)

api.add_resource(AreaController,'/areas','/areas/<id>')

api.add_resource(EmployeeController,'/empleado')

if __name__ == '__main__':
    app.run(debug = True)