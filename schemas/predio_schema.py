from utils.ma import ma
from marshmallow import fields
from schemas.tipo_predio_schema import tipoPredio_schema

class Meta:
    model = Predio
    
    fields = (
        
    )
    
    tipo_predio = ma.Nested(TipoPredioSchema)
    
    
Predio_schema = PredioSchema()
Predios_schema = PrediosSchema(many = True)