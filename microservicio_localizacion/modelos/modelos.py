import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()

class Localizacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado_sensor_ambiente = db.Column(db.Boolean)
    estado_sensor_puesta_ventana = db.Column(db.Boolean)
    estado_sensor_signos_vitales = db.Column(db.Boolean)
    fecha_evento = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class LocalizacionSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Localizacion
         load_instance = True