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
import random

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


def autenticarOperador(usuario):
    try:
        
        print("entro")
        content = requests.post('http://127.0.0.1:5002/signin', json = usuario)
        if content.status_code == 404:
            return content.json(), 404
        else:
            return content.json()
    except ValueError:
        print("Se perdió la conexión")



starttime = time.time()
operadores = [{"usuario": "operador1","contrasena": "1234"},{"usuario": "operador2","contrasena": "12342"},{"usuario": "operador3","contrasena": "12343"},{"usuario": "operador4","contrasena": "12344"},{"usuario": "operador5","contrasena": "1235"}\
    ,{"usuario": "operador1","contrasena": "111"},{"usuario": "operador2","contrasena": "111"},{"usuario": "operador3","contrasena": "111"},{"usuario": "operador4","contrasena": "111"},{"usuario": "operador5","contrasena": "111"}]

while True:


    #usuario = {"usuario": "operador1","contrasena": "1234"}
    result = autenticarOperador(random.choice(operadores))
    print(result)
    # if result == 'Conection lost':
    #     os.chdir(r"C:\Users\CrackMayo\Desktop\Experimento_Disponiblidad_Montorio_ABC\microservicio_localizacion")
    #     proc = subprocess.Popen(['flask', 'run', '-p', '5001'])

    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
