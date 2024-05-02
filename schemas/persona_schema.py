from utils.ma import ma
from marshmallow import fields

class PersonaSchema(ma.Schema): 
    id_persona = fields.Integer()
    apellido_paterno = fields.String()
    apellido_materno = fields.String()
    nombres = fields.String()
    fecha_nacimiento = fields.Date()
    id_tipo_documento = fields.Integer()
    ndocumento = fields.String()
    direccion = fields.String()
    idubigeo = fields.String()

persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)