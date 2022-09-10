from microservicio_localizacion import create_app
from flask_restful import Resource, Api
from flask import Flask


app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaEstadoLocalizaciones(Resource):
    def get(self):
        return True

api.add_resource(VistaEstadoLocalizaciones, '/localizaciones/estado')
