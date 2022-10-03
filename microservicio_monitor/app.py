import json
from microservicio_monitor import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from microservicio_monitor.modelos.modelos import Monitor
from .modelos import db
import requests
import json 
import time
from flask import request
from .modelos import db, Monitor, MonitorSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
import random
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)


class VistaMonitorearEstadoAutenticaciones(Resource):
    def post(self):
        nuevo_registro = Monitor(habilitado=request.json["habilitado"], registro=request.json["registro"],usuario=request.json["usuario"])
        db.session.add(nuevo_registro)
        db.session.commit()
        if nuevo_registro.registro == 'IP Valida':
            return {"mensaje": "Acceso confiable", "bloqueo": False}
        else:
            return {"mensaje": "Acceso no confiable", "bloqueo": True}
                    
api.add_resource(VistaMonitorearEstadoAutenticaciones, '/monitoreo/habilitado/')


# x = VistaMonitorearEstadoAutenticaciones()
# starttime = time.time()
# while True:
#     result = x.get()
#     print(result)
#     # if result == 'Conection lost':
#     #     os.chdir(r"C:\Users\CrackMayo\Desktop\Experimento_Disponiblidad_Montorio_ABC\microservicio_localizacion")
#     #     proc = subprocess.Popen(['flask', 'run', '-p', '5001'])

#     time.sleep(1.0 - ((time.time() - starttime) % 1.0))




# while True:


#     #usuario = {"usuario": "operador1","contrasena": "1234"}
#     result = autenticarOperador(random.choice(operadores))
#     print(result)
#     # if result == 'Conection lost':
#     #     os.chdir(r"C:\Users\CrackMayo\Desktop\Experimento_Disponiblidad_Montorio_ABC\microservicio_localizacion")
#     #     proc = subprocess.Popen(['flask', 'run', '-p', '5001'])

#     time.sleep(5.0 - ((time.time() - starttime) % 5.0))



