import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()

class SensorAmbiente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.Boolean)
    fecha_evento = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class SensorAmbienteSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = SensorAmbiente
         load_instance = True