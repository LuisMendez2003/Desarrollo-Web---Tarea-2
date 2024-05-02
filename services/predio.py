from flask import Blueprint, request, jsonify
from model.predio import Predio
from utils.db import db

#Creación de una instancia Blueprint, para cuando exista
#más de una carpeta models?
predio = Blueprint('predio', __name__)

#METODOS GET (CRUD = READ)
@predio.route('/predios/v1', methods = ['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-backend'
    return jsonify(result)

@predio.route('/predios/v1/listar', methods = ['GET'])
def getPredios():
    result = {}
    predios = Predio.query.all() #"Select from Predio"
    result["data"] = predios
    result["status_cod"] = 200 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Contacts were recovery succesfully..."
    return jsonify(result), 200

@predio.route('/predios/<int:id>', methods = ['GET'])
def getPredio(id):
    result = {}
    predio = Predio.query.get(id) #"Select from Contact"
    result["data"] = predio
    result["status_cod"] = 200 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Contacts were recovery succesfully..."
    return jsonify(result), 200

###METODOS INSERTAR  POST  (CRUD = CREATE)

@predio.route('/predios/v1/insert', methods = ['POST'])
def insert():
    result = {}
    body = request.get_json()
    id_tipo_predio = body.get('id_tipo_predio')
    descripcion = body.get('descripcion')
    ruc = body.get('ruc')
    telefono = body.get('telefono')
    correo = body.get('correo')
    direccion = body.get('direccion')
    idubigeo = body.get('idubigeo')
    
    
    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_cod"] = 400 #Status_code se envia como resultado del query para FrontEnd
        result["status_msg"] = "Data is missing"
        return jsonify(result), 400
    
    predio = Predio(id_tipo_predio, descripcion, ruc, telefono, correo, direccion,idubigeo)
    db.session.add(predio) #"INSERT into ..."
    db.session.commit()
    result["data"] = predio
    result["status_cod"] = 201 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Data was created"
    return jsonify(result), 201

###METODOS UPDATE  POST  (CRUD = UPDATE)

@predio.route('/predios/v1/update', methods = ['POST'])
def update():
    result = {}
    body = request.get_json()
    id_predio = body.get('id_predio')
    id_tipo_predio = body.get('id_tipo_predio')
    descripcion = body.get('descripcion')
    ruc = body.get('ruc')
    telefono = body.get('telefono')
    correo = body.get('correo')
    direccion = body.get('direccion')
    idubigeo = body.get('idubigeo')
    
    #if data is missing
    if not id_predio or not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo:
        result["status_cod"] = 400 #Status_code se envia como resultado del query para FrontEnd
        result["status_msg"] = "Data is missing"
        return jsonify(result), 400
    
    predio = Predio.query.get(id_predio) #"Selecto from contacto where id = ..."
    
    #if id is not found
    if not predio:
        result["status_cod"] = 400 #Status_code se envia como resultado del query para FrontEnd
        result["status_msg"] = "ID does not exist"
        return jsonify(result), 400
    
    #modifies
    predio.id_tipo_precio = id_tipo_predio
    predio.descripcion = descripcion
    predio.ruc = ruc
    predio.telefono = telefono
    predio.correo = correo
    predio.direccion = direccion
    predio.idubigeo = idubigeo
    db.session.commit()
    
    #sends result
    result["data"] = predio
    result["status_cod"] = 202 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Data was modified"
    return jsonify(result), 202

###METODOS UPDATE  POST  (CRUD = delete)
@predio.route('/predios/v1/delete', methods = ['DELETE'])
def delete():
    result = {}
    body = request.get_json()
    id_predio = body.get('id_predio')    

#if id is missing
    if not id_predio:
        result["status_cod"] = 400 #Status_code se envia como resultado del query para FrontEnd
        result["status_msg"] = "ID must be provided"
        return jsonify(result), 400
    
    predio = Predio.query.get(id_predio) #"Selecto from contacto where id = ..."
    
    #if id is not found
    if not predio:
        result["status_cod"] = 400 #Status_code se envia como resultado del query para FrontEnd
        result["status_msg"] = "ID does not exist"
        return jsonify(result), 400
    
    db.session.delete(predio) #deletes contacto
    db.session.commit() #confirm changes
    
    #sends result
    result["data"] = predio
    result["status_cod"] = 200 #Status_code se envia como resultado del query para FrontEnd
    result["status_msg"] = "Data was deleted"
    return jsonify(result), 200