import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()

class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(50))
    habilitado = db.Column(db.Boolean, default=True)
    registro = db.Column(db.String(128))
    fecha_evento = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class MonitorSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Monitor
         load_instance = True