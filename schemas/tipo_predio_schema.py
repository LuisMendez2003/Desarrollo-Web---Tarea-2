from utils.ma import ma
from marshmallow import fields

class TipoPredioSchema(ma.Schema):
    id_tipo_predio = fields.Integer()
    nomre_predio = fields.String()

tipoPredio_schema = TipoPredioSchema()
tiposPredio_schema = TipoPredioSchema(many=True)