from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.estudiante.EstudianteDao import EstudianteDao

estudiante_api = Blueprint('estudiante_api', __name__)

# Trae todos los estudiantes
@estudiante_api.route('/estudiantes', methods=['GET'])
def getEstudiantes():
    estudiante_dao = EstudianteDao()

    try:
        estudiantes = estudiante_dao.getEstudiantes()
        return jsonify({
            'success': True,
            'data': estudiantes,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los estudiantes: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Obtener un estudiante específico por ID
@estudiante_api.route('/estudiantes/<int:id_estudiante>', methods=['GET'])
def getEstudiante(id_estudiante):
    estudiante_dao = EstudianteDao()

    try:
        estudiante = estudiante_dao.getEstudianteById(id_estudiante)
        if estudiante:
            return jsonify({
                'success': True,
                'data': estudiante,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el estudiante con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener estudiante: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agregar un nuevo estudiante
@estudiante_api.route('/estudiantes', methods=['POST'])
def addEstudiante():
    data = request.get_json()
    estudiante_dao = EstudianteDao()

    # Validar campos obligatorios
    campos_requeridos = ['id_persona', 'curso']
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(str(data[campo]).strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        id_estudiante = estudiante_dao.guardarEstudiante(data['id_persona'], data['curso'])
        if id_estudiante:
            return jsonify({
                'success': True,
                'data': {'id_estudiante': id_estudiante},
                'error': None
            }), 201
        else:
            return jsonify({'success': False, 'error': 'No se pudo guardar el estudiante. Consulte con el administrador.'}), 500
    except Exception as e:
        app.logger.error(f"Error al agregar estudiante: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Actualizar un estudiante
@estudiante_api.route('/estudiantes/<int:id_estudiante>', methods=['PUT'])
def updateEstudiante(id_estudiante):
    data = request.get_json()
    estudiante_dao = EstudianteDao()

    # Validar campos obligatorios
    campos_requeridos = ['curso']
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(str(data[campo]).strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        if estudiante_dao.updateEstudiante(id_estudiante, data['curso']):
            return jsonify({
                'success': True,
                'data': {'id_estudiante': id_estudiante},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el estudiante con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar estudiante: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Eliminar un estudiante
@estudiante_api.route('/estudiantes/<int:id_estudiante>', methods=['DELETE'])
def deleteEstudiante(id_estudiante):
    estudiante_dao = EstudianteDao()

    try:
        if estudiante_dao.deleteEstudiante(id_estudiante):
            return jsonify({
                'success': True,
                'mensaje': f'Estudiante con ID {id_estudiante} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el estudiante con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar estudiante: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
