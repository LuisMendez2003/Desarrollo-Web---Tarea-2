from utils.db import db
class TipoPredio(db.Model):
    __tablename__ = 'tipo_predio'
    id_tipo_predio = db.Column(db.Integer, primary_key=True)
    nomre_predio = db.Column(db.String(255))

    def __init__(self, id_tipo_predio, nombre_predio):
        self.id_tipo_predio = id_tipo_predio
        self.nomre_predio = nombre_predio