import json
from microservicio_monitor import create_app
from flask_restful import Resource, Api
from flask import Flask, request

from microservicio_monitor.modelos.modelos import Monitor
from .modelos import db
import requests
import json 
import time
import subprocess
import os
from flask import request
from .modelos import db, Monitor, MonitorSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)

class VistaMonitorearEstadoLocalizacion(Resource):
    def get(self):
        try:
            content = requests.get('http://127.0.0.1:5001/localizaciones/estado')
            estado_localizaciones = all(content.json())
            nuevo_registro = Monitor(estado_localizacion=estado_localizaciones, localizacion='Localizacion_de_prueba')
            db.session.add(nuevo_registro)
            db.session.commit()
            if content.status_code == 404:
                return content.json(), 404
            else:
                return content.json()
                
        except: 
            return 'Conection lost'  
api.add_resource(VistaMonitorearEstadoLocalizacion, '/monitoreo/localizaciones')


x = VistaMonitorearEstadoLocalizacion()
starttime = time.time()
while True:
    result = x.get()
    print(result)
    # if result == 'Conection lost':
    #     os.chdir(r"C:\Users\CrackMayo\Desktop\Experimento_Disponiblidad_Montorio_ABC\microservicio_localizacion")
    #     proc = subprocess.Popen(['flask', 'run', '-p', '5001'])

    time.sleep(1.0 - ((time.time() - starttime) % 1.0))


