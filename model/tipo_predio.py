from utils.db import db
from dataclasses import dataclass

@dataclass
class Tipo_Predio(db.Model):
    id_tipo_predio: int
    nomre_predio: str
    
    #Correspondencia con DB
    id_tipo_predio = db.Column(db.Integer, primary_key = True)
    nomre_predio = db.Column(db.String(80))
    
    
    def __init__(self, nomre_predio):
        self.nomre_predio = nomre_predio