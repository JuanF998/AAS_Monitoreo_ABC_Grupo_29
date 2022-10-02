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

class VistaMonitorearEstadoAutenticaciones(Resource):
    def get(self):
        content = requests.get('http://127.0.0.1:5001/autenticacion/habilitado')
        habilitado_autenticacion = all(content.json())
        if habilitado_autenticacion:
            nuevo_registro = Monitor(habilitado_autenticacion=habilitado_autenticacion, registro='IP Valida')
            db.session.add(nuevo_registro)
            db.session.commit()
            if content.status_code == 404:
                return content.json(), 404
            else:
                return content.json()
        else:
            nuevo_registro = Monitor(habilitado_autenticacion=habilitado_autenticacion, registro='IP NO Valida')
            db.session.add(nuevo_registro)
            db.session.commit()
            if content.status_code == 404:
                return content.json(), 404
            else:
                return content.json()
                    
api.add_resource(VistaMonitorearEstadoAutenticaciones, '/monitoreo/habilitado')


x = VistaMonitorearEstadoAutenticaciones()
starttime = time.time()
while True:
    result = x.get()
    print(result)
    # if result == 'Conection lost':
    #     os.chdir(r"C:\Users\CrackMayo\Desktop\Experimento_Disponiblidad_Montorio_ABC\microservicio_localizacion")
    #     proc = subprocess.Popen(['flask', 'run', '-p', '5001'])

    time.sleep(1.0 - ((time.time() - starttime) % 1.0))


