from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.asignatura.AsignaturaDao import AsignaturaDao

asignatura_api = Blueprint('asignatura_api', __name__)

# Obtener todas las asignaturas
@asignatura_api.route('/asignaturas', methods=['GET'])
def getAsignaturas():
    asignatura_dao = AsignaturaDao()

    try:
        asignaturas = asignatura_dao.getAsignaturas()

        return jsonify({
            'success': True,
            'data': asignaturas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las asignaturas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Obtener una asignatura por ID
@asignatura_api.route('/asignaturas/<int:asignatura_id>', methods=['GET'])
def getAsignatura(asignatura_id):
    asignatura_dao = AsignaturaDao()

    try:
        asignatura = asignatura_dao.getAsignaturaById(asignatura_id)

        if asignatura:
            return jsonify({
                'success': True,
                'data': asignatura,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la asignatura con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener asignatura: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agregar una nueva asignatura
@asignatura_api.route('/asignaturas', methods=['POST'])
def addAsignatura():
    data = request.get_json()
    asignatura_dao = AsignaturaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre_estudiante', 'curso', 'asignatura']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        nombre_estudiante = data['nombre_estudiante']
        curso = data['curso']
        asignatura = data['asignatura']

        asignatura_id = asignatura_dao.guardarAsignatura(nombre_estudiante, curso, asignatura)
        if asignatura_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': asignatura_id, 'nombre_estudiante': nombre_estudiante, 'curso': curso, 'asignatura': asignatura},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la asignatura. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar asignatura: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Actualizar una asignatura existente
@asignatura_api.route('/asignaturas/<int:asignatura_id>', methods=['PUT'])
def updateAsignatura(asignatura_id):
    data = request.get_json()
    asignatura_dao = AsignaturaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre_estudiante', 'curso', 'asignatura']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    nombre_estudiante = data['nombre_estudiante']
    curso = data['curso']
    asignatura = data['asignatura']

    try:
        if asignatura_dao.updateAsignatura(asignatura_id, nombre_estudiante, curso, asignatura):
            return jsonify({
                'success': True,
                'data': {'id': asignatura_id, 'nombre_estudiante': nombre_estudiante, 'curso': curso, 'asignatura': asignatura},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la asignatura con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar asignatura: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Eliminar una asignatura
@asignatura_api.route('/asignaturas/<int:asignatura_id>', methods=['DELETE'])
def deleteAsignatura(asignatura_id):
    asignatura_dao = AsignaturaDao()

    try:
        if asignatura_dao.deleteAsignatura(asignatura_id):
            return jsonify({
                'success': True,
                'mensaje': f'Asignatura con ID {asignatura_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la asignatura con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar asignatura: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
