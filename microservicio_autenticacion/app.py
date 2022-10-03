from random import random
from microservicio_autenticacion import create_app
from flask import Flask, request
from flask_restful import Api
from microservicio_autenticacion.modelos.modelos import Usuario
from .modelos import db
from .vistas import VistaLogIn
import requests
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

import time
import random


app = create_app('default')
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()
api = Api(app)
jwt = JWTManager(app)

api.add_resource(VistaLogIn, '/signin')

# def autenticarOperador(usuario):
#     try:
        
#         print("entro")
#         content = requests.post('http://127.0.0.1:5002/signin', json = usuario)
#         if content.status_code == 404:
#             return content.json(), 404
#         else:
#             token_de_acceso = create_access_token(identity="operador1")
#             print(token_de_acceso)
#             return content.json()
#     except ValueError:
#         print("Se perdió la conexión")


# starttime = time.time()
# operadores = [{"usuario": "operador1","contrasena": "1234"},{"usuario": "operador2","contrasena": "12342"},{"usuario": "operador3","contrasena": "12343"},{"usuario": "operador4","contrasena": "12344"},{"usuario": "operador5","contrasena": "1235"}\
#     ,{"usuario": "operador1","contrasena": "111"},{"usuario": "operador2","contrasena": "111"},{"usuario": "operador3","contrasena": "111"},{"usuario": "operador4","contrasena": "111"},{"usuario": "operador5","contrasena": "111"}]
# while True:


#     #usuario = {"usuario": "operador1","contrasena": "1234"}
#     result = autenticarOperador(random.choice(operadores))
#     print(result)
#     # if result == 'Conection lost':
#     #     os.chdir(r"C:\Users\CrackMayo\Desktop\Experimento_Disponiblidad_Montorio_ABC\microservicio_localizacion")
#     #     proc = subprocess.Popen(['flask', 'run', '-p', '5001'])

#     time.sleep(5.0 - ((time.time() - starttime) % 5.0))
