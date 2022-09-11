from microservicio_localizacion import create_app
from flask_restful import Resource, Api
from flask import Flask
import requests

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaEstadoLocalizaciones(Resource):
    def get(self):
        try:
            content = requests.get('http://127.0.0.1:5003/sensor/estado')
            
            if content.status_code == 404:
                return content.json(), 404
            else:
                return content.json()
        except: 
            return 'Conection lost'  

api.add_resource(VistaEstadoLocalizaciones, '/localizaciones/estado')
