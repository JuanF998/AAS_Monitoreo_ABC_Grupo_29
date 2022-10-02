from flask import request
from microservicio_autenticacion.modelos.modelos import Usuario
from ..modelos import db, UsuarioSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
usuario_schema = UsuarioSchema()

class VistaLogIn(Resource):

    def post(self):
        print(request.remote_addr)
        print(request.json["usuario"])
        print(request.json["contrasena"])
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"], Usuario.contrasena == request.json["contrasena"]).first()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            if(usuario.ip_autorizada == request.remote_addr):
                if(usuario.habilitado == True):
                    additional_claims = {"permiso": usuario.permiso}
                    #asigna al body del jwt los permisos que tiene acceso el usuario
                    token_de_acceso = create_access_token(identity=usuario.id,additional_claims=additional_claims)                    
                    return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso}
                else:
                    return "El usuario se encuentra desactivado", 401
            return "El usuario no está autorizado desde el origen de conexion", 401

    def get(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"], Usuario.contrasena == request.json["contrasena"]).first()
        return usuario.habilitado
