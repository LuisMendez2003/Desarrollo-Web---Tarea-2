from utils.db import db

class Persona(db.Model):
    __tablename__ = 'persona'
    
    id_persona = db.Column(db.Integer, primary_key=True)
    
    apellido_paterno = db.Column(db.String(60))
    apellido_materno = db.Column(db.String(60))
    nombres = db.Column(db.String(60))
    fecha_nacimiento = db.Column(db.Date)
    id_tipo_documento = db.Column(db.Integer)
    ndocumento = db.Column(db.String(15))
    direccion = db.Column(db.String(150))
    idubigeo = db.Column(db.String(6))

    def __init__(self, id_persona, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, id_tipo_documento, ndocumento, direccion, idubigeo):
        self.id_persona = id_persona
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.nombres = nombres
        self.fecha_nacimiento = fecha_nacimiento
        self.id_tipo_documento = id_tipo_documento
        self.ndocumento = ndocumento
        self.direccion = direccion
        self.idubigeo = idubigeo