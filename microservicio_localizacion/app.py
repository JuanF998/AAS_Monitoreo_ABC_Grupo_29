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
        estados_sensores = []
        try:
            content1 = requests.get('http://127.0.0.1:5003/sensor_ambiente/estado')
            estados_sensores.append(content1.json())
        except: 
            estados_sensores.append(False) 

        try:
            content2 = requests.get('http://127.0.0.1:5004/sensor_puertas_ventanas/estado')
            estados_sensores.append(content2.json())
        except: 
            estados_sensores.append(False) 

        try:
            content3 = requests.get('http://127.0.0.1:5005/sensor_signos_vitales/estado')
            estados_sensores.append(content3.json())
        except: 
            estados_sensores.append(False) 
            
        return estados_sensores



api.add_resource(VistaEstadoLocalizaciones, '/localizaciones/estado')
