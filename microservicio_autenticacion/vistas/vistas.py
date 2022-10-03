from flask import request
import requests
from microservicio_autenticacion.modelos.modelos import Usuario
from ..modelos import db, UsuarioSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
import json
usuario_schema = UsuarioSchema()

class VistaLogIn(Resource):

    def post(self):
        print("IP:", request.remote_addr)
        url_monitor='http://127.0.0.1:5001/monitoreo/habilitado/'
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"], Usuario.contrasena == request.json["contrasena"]).first()
        if usuario is None:
            monitor={"usuario":request.json["usuario"],"registro":"Login invalido","habilitado":False}
            content = requests.post(url_monitor, json = monitor)    
            respuesta_monitor=content.json()
            # if(respuesta_monitor["bloqueo"]==True):
            #     usuario.habilitado = False
            #     db.session.commit()            
            return "El usuario no existe", 404
        else:
            if(usuario.ip_autorizada == request.remote_addr):
                if(usuario.habilitado == True):
                    monitor={
                        "usuario":usuario.usuario,
                        "registro":"IP Valida",
                        "habilitado":usuario.habilitado
                    }
                    print("antes")
                    content = requests.post(url_monitor, json = monitor)    
                    respuesta_monitor=content.json()
                    if(respuesta_monitor["bloqueo"]==True):
                        usuario.habilitado = False
                        db.session.commit()
                        return "El usuario se encuentra desactivado1", 401
                    else:
                        additional_claims = {"permiso": usuario.permiso}
                        #asigna al body del jwt los permisos que tiene acceso el usuario
                        token_de_acceso = create_access_token(identity=usuario.id,additional_claims=additional_claims)                    
                        return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso}
                else:
                    return "El usuario se encuentra desactivado", 401
            else:
                #Bloqueo Ip No Valida
                monitor={
                        "usuario":usuario.usuario,
                        "registro":"IP No Valida",
                        "habilitado":usuario.habilitado
                    }
                content = requests.post(url_monitor, json = monitor)    
                respuesta_monitor=content.json()
                if(respuesta_monitor["bloqueo"]==True):
                    usuario.habilitado = False
                    db.session.commit()
                return "El usuario no está autorizado desde el origen de conexion(ip no valida)", 401
                
            #return "El usuario no está autorizado desde el origen de conexion", 401

    def get(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"], Usuario.contrasena == request.json["contrasena"]).first()
        return usuario.habilitado