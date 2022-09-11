import json
from microservicio_sensor_puerta_ventana import create_app
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

class VistaEnviarEstadoSensorPuertasVentanas(Resource):
    def get(self):
        return True

api.add_resource(VistaEnviarEstadoSensorPuertasVentanas, '/sensor_puertas_ventanas/estado')