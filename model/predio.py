from utils.db import db
from model.tipo_predio import TipoPredio
from model.ubigeo import Ubigeo
from model.persona import Persona

class Predio(db.Model):
    __tablename__ = 'predio'
    id_predio = db.Column(db.Integer, primary_key=True)
    id_tipo_predio = db.Column(db.Integer, db.ForeignKey('tipo_predio.id_tipo_predio'))
    descripcion = db.Column(db.String(255))
    ruc = db.Column(db.String(11))
    telefono = db.Column(db.String(20))
    correo = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    idubigeo = db.Column(db.String(6), db.ForeignKey('ubigeo.idubigeo'))
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    url_imagen = db.Column(db.String(255))
    total_mdu = db.Column(db.Integer)


    tipo_predio = db.relationship('TipoPredio', backref='predio')
    ubigeo = db.relationship('Ubigeo', backref='predio')
    personas = db.relationship('Persona', backref='predio')

    def __init__(self, id_predio, id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo, id_persona, url_imagen, total_mdu):
        self.id_predio = id_predio
        self.id_tipo_predio = id_tipo_predio
        self.descripcion = descripcion
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.idubigeo = idubigeo
        self.id_persona = id_persona
        self.url_imagen = url_imagen
        self.total_mdu = total_mdu

    def __init__(self, id_predio, id_tipo_predio, descripcion, ruc, telefono, correo, direccion):
        self.id_predio = id_predio
        self.id_tipo_predio = id_tipo_predio
        self.descripcion = descripcion
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion