from utils.db import db

class Ubigeo(db.Model):
    __tablename__ = 'ubigeo'
    
    idubigeo = db.Column(db.String(6), primary_key=True)
    departamento = db.Column(db.String(60))

    def __init__(self, idubigeo, departamento):
        self.idubigeo = idubigeo
        self.departamento = departamento