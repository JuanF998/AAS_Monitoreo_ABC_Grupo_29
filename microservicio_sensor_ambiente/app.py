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

class VistaEnviarEstadoSensor(Resource):
    def get(self):
        return True

api.add_resource(VistaEnviarEstadoSensor, '/sensor/estado')