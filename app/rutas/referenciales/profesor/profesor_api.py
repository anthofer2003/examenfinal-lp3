from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.profesor.ProfesorDao import ProfesorDao

profesor_api = Blueprint('profesor_api', __name__)

# Trae todos los profesores
@profesor_api.route('/profesores', methods=['GET'])
def getProfesores():
    profesor_dao = ProfesorDao()

    try:
        profesores = profesor_dao.getProfesores()
        return jsonify({
            'success': True,
            'data': profesores,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los profesores: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@profesor_api.route('/profesores/<int:id_profesor>', methods=['GET'])
def getProfesor(id_profesor):
    profesor_dao = ProfesorDao()

    try:
        profesor = profesor_dao.getProfesorById(id_profesor)

        if profesor:
            return jsonify({
                'success': True,
                'data': profesor,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el profesor con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener profesor: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo profesor
@profesor_api.route('/profesores', methods=['POST'])
def addProfesor():
    data = request.get_json()
    profesor_dao = ProfesorDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['id_persona', 'asignatura', 'salario']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        id_profesor = profesor_dao.guardarProfesor(data['id_persona'], data['asignatura'], data['salario'])
        if id_profesor:
            return jsonify({
                'success': True,
                'data': {'id_profesor': id_profesor},
                'error': None
            }), 201
        else:
            return jsonify({'success': False, 'error': 'No se pudo guardar el profesor. Consulte con el administrador.'}), 500
    except Exception as e:
        app.logger.error(f"Error al agregar profesor: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@profesor_api.route('/profesores/<int:id_profesor>', methods=['PUT'])
def updateProfesor(id_profesor):
    data = request.get_json()
    profesor_dao = ProfesorDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['asignatura', 'salario']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        if profesor_dao.updateProfesor(id_profesor, data['asignatura'], data['salario']):
            return jsonify({
                'success': True,
                'data': {'id_profesor': id_profesor},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el profesor con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar profesor: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@profesor_api.route('/profesores/<int:id_profesor>', methods=['DELETE'])
def deleteProfesor(id_profesor):
    profesor_dao = ProfesorDao()

    try:
        if profesor_dao.deleteProfesor(id_profesor):
            return jsonify({
                'success': True,
                'mensaje': f'Profesor con ID {id_profesor} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el profesor con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar profesor: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
