from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from model.predio import Predio
from schemas.predio_schema import predio_schema, predios_schema

predio_routes = Blueprint("predio_routes", __name__)

@predio_routes.route('/predio', methods=['POST'])
def create_Predio():
    id_tipo_predio = request.json.get('id_tipo_predio')
    descripcion = request.json.get('descripcion')
    ruc = request.json.get('ruc')
    telefono = request.json.get('telefono')
    correo = request.json.get('correo')
    direccion = request.json.get('direccion')
    idubigeo = request.json.get('idubigeo')
    id_persona = request.json.get('id_persona')

    new_predio = Predio(id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo, id_persona)

    db.session.add(new_predio)
    db.session.commit()

    result = predio_schema.dump(new_predio)

    data = {
        'message': 'Nuevo Predio creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@predio_routes.route('/predio', methods=['GET'])
def get_Predios():
    all_predios = Predio.query.all()
    result = predios_schema.dump(all_predios)

    data = {
        'message': 'Todos los Predios',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@predio_routes.route('/predio/<int:id>', methods=['GET'])
def get_Predio(id):
    predio = Predio.query.get(id)

    if not predio:
        data = {
            'message': 'Predio no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = predio_schema.dump(predio)

    data = {
        'message': 'Predio encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@predio_routes.route('/predio/<int:id>', methods=['PUT'])
def update_Predio(id):
    predio = Predio.query.get(id)

    if not predio:
        data = {
            'message': 'Predio no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_tipo_predio = request.json.get('id_tipo_predio')
    descripcion = request.json.get('descripcion')
    ruc = request.json.get('ruc')
    telefono = request.json.get('telefono')
    correo = request.json.get('correo')
    direccion = request.json.get('direccion')
    idubigeo = request.json.get('idubigeo')
    id_persona = request.json.get('id_persona')

    predio.id_tipo_predio = id_tipo_predio
    predio.descripcion = descripcion
    predio.ruc = ruc
    predio.telefono = telefono
    predio.correo = correo
    predio.direccion = direccion
    predio.idubigeo = idubigeo
    predio.id_persona = id_persona

    db.session.commit()

    result = predio_schema.dump(predio)

    data = {
        'message': 'Predio actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@predio_routes.route('/predio/<int:id>', methods=['DELETE'])
def delete_Predio(id):
    predio = Predio.query.get(id)

    if not predio:
        data = {
            'message': 'Predio no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(predio)
    db.session.commit()

    data = {
        'message': 'Predio eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)