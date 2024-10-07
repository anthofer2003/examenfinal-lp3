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

# Trae un estudiante por ID
@estudiante_api.route('/estudiantes/<int:estudiante_id>', methods=['GET'])
def getEstudiante(estudiante_id):
    estudiante_dao = EstudianteDao()

    try:
        estudiante = estudiante_dao.getEstudianteById(estudiante_id)

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

# Agrega un nuevo estudiante
@estudiante_api.route('/estudiantes', methods=['POST'])
def addEstudiante():
    data = request.get_json()
    estudiante_dao = EstudianteDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'direccion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre = data['nombre'].upper()
        apellido = data['apellido'].upper()
        fecha_nacimiento = data['fecha_nacimiento']  # Asegúrate de que este dato esté en el formato correcto
        telefono = data['telefono']
        direccion = data['direccion'].upper()

        if estudiante_dao.guardarEstudiante(nombre, apellido, fecha_nacimiento, telefono, direccion):
            return jsonify({
                'success': True,
                'data': {
                    'nombre': nombre,
                    'apellido': apellido,
                    'fecha_nacimiento': fecha_nacimiento,
                    'telefono': telefono,
                    'direccion': direccion
                },
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar el estudiante. Consulte con el administrador.'
            }), 500

    except Exception as e:
        app.logger.error(f"Error al agregar estudiante: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Actualiza un estudiante
@estudiante_api.route('/estudiantes/<int:estudiante_id>', methods=['PUT'])
def updateEstudiante(estudiante_id):
    data = request.get_json()
    estudiante_dao = EstudianteDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'direccion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    nombre = data['nombre'].upper()
    apellido = data['apellido'].upper()
    fecha_nacimiento = data['fecha_nacimiento']
    telefono = data['telefono']
    direccion = data['direccion'].upper()

    try:
        if estudiante_dao.updateEstudiante(estudiante_id, nombre, apellido, fecha_nacimiento, telefono, direccion):
            return jsonify({
                'success': True,
                'data': {
                    'id': estudiante_id,
                    'nombre': nombre,
                    'apellido': apellido,
                    'fecha_nacimiento': fecha_nacimiento,
                    'telefono': telefono,
                    'direccion': direccion
                },
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

# Elimina un estudiante
@estudiante_api.route('/estudiantes/<int:estudiante_id>', methods=['DELETE'])
def deleteEstudiante(estudiante_id):
    estudiante_dao = EstudianteDao()

    try:
        if estudiante_dao.deleteEstudiante(estudiante_id):
            return jsonify({
                'success': True,
                'mensaje': f'Estudiante con ID {estudiante_id} eliminado correctamente.',
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
