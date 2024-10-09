from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.facultad.FacultadDao import FacultadDao

facultad_api = Blueprint('facultad_api', __name__)

# Trae todas las facultades
@facultad_api.route('/facultades', methods=['GET'])
def getFacultades():
    facultad_dao = FacultadDao()

    try:
        facultades = facultad_dao.getFacultades()

        return jsonify({
            'success': True,
            'data': facultades,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las facultades: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Trae una facultad por su ID
@facultad_api.route('/facultades/<int:facultad_id>', methods=['GET'])
def getFacultad(facultad_id):
    facultad_dao = FacultadDao()

    try:
        facultad = facultad_dao.getFacultadById(facultad_id)

        if facultad:
            return jsonify({
                'success': True,
                'data': facultad,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la facultad con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener la facultad: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva facultad
@facultad_api.route('/facultades', methods=['POST'])
def addFacultad():
    data = request.get_json()
    facultad_dao = FacultadDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'ubicacion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        nombre = data['nombre'].upper()
        ubicacion = data['ubicacion'].upper()

        facultad_id = facultad_dao.guardarFacultad(nombre, ubicacion)
        if facultad_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': facultad_id, 'nombre': nombre, 'ubicacion': ubicacion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la facultad. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar facultad: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Actualiza una facultad existente
@facultad_api.route('/facultades/<int:facultad_id>', methods=['PUT'])
def updateFacultad(facultad_id):
    data = request.get_json()
    facultad_dao = FacultadDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'ubicacion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    nombre = data['nombre'].upper()
    ubicacion = data['ubicacion'].upper()

    try:
        if facultad_dao.updateFacultad(facultad_id, nombre, ubicacion):
            return jsonify({
                'success': True,
                'data': {'id': facultad_id, 'nombre': nombre, 'ubicacion': ubicacion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la facultad con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar facultad: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Elimina una facultad
@facultad_api.route('/facultades/<int:facultad_id>', methods=['DELETE'])
def deleteFacultad(facultad_id):
    facultad_dao = FacultadDao()

    try:
        if facultad_dao.deleteFacultad(facultad_id):
            return jsonify({
                'success': True,
                'mensaje': f'Facultad con ID {facultad_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la facultad con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar facultad: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
