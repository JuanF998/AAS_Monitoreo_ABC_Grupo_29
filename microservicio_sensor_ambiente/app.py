import json
import random
from microservicio_sensor_ambiente import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from .modelos import db
import requests
import json 
import time
import subprocess
import os
from flask import request
from .modelos import db, SensorAmbiente, SensorAmbienteSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)

class VistaEnviarEstadoSensorAmbiente(Resource):
    def get(self):
        estado_sensor = bool(random.getrandbits(1))
        nuevo_registro = SensorAmbiente(estado = estado_sensor)
        db.session.add(nuevo_registro)
        db.session.commit()
        return estado_sensor

api.add_resource(VistaEnviarEstadoSensorAmbiente, '/sensor_ambiente/estado')