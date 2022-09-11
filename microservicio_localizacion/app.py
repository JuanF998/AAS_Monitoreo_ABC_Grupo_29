from microservicio_localizacion import create_app
from flask_restful import Resource, Api
from flask import Flask
import requests

from microservicio_monitor.modelos.modelos import Monitor
from .modelos import db
import requests
import json 
import time
import subprocess
import os
from flask import request
from .modelos import db, Localizacion, LocalizacionSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

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

        nuevo_registro = Localizacion(estado_sensor_ambiente=estados_sensores[0], estado_sensor_puesta_ventana=estados_sensores[1], estado_sensor_signos_vitales=estados_sensores[2])
        db.session.add(nuevo_registro)
        db.session.commit()
            
        return estados_sensores



api.add_resource(VistaEstadoLocalizaciones, '/localizaciones/estado')
