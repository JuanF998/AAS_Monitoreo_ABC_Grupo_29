import json
from microservicio_monitor import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json 
import time
import subprocess
import os


app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaMonitorearEstadoLocalizacion(Resource):
    def get(self):
        try:
            content = requests.get('http://127.0.0.1:5001/localizaciones/estado')
            
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


