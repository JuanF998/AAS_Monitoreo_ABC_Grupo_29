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

def autenticarOperador(self):
    try:
        usuario = {
            "usuario": "operador1",
            "contrasena": "1234"
        }
        content = requests.post('http://127.0.0.1:5000/signin', json = usuario)
        if content.status_code == 404:
            return content.json(), 404
        else:
            return content.json()
    except ValueError:
        print("Se perdió la conexión")