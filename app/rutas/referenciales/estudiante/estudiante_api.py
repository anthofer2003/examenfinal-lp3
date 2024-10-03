from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.estudiante.EstudianteDao import EstudianteDao
from datetime import datetime

estudiante_api = Blueprint('estudiante_api', __name__)

# Trae todos los estudiantes
@estudiante_api.route('/estudiantes', methods=['GET'])
def getEstudiantes():
    estudiante_dao = EstudianteDao()

    try:
        estudiantes = estudiante_dao.getEstudiantes()
        # Formatea la lista de estudiantes a un formato que puedes enviar como JSON
        estudiantes_json = [{
            'id_estudiante': est.id_estudiante,
            'nombre': est.nombre,
            'apellido': est.apellido,
            'fecha_de_nacimiento': est.fecha_de_nacimiento.strftime('%Y-%m-%d'),
            'telefono': est.telefono,
            'direccion': est.direccion
        } for est in estudiantes]

        return jsonify({
            'success': True,
            'data': estudiantes_json,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los estudiantes: {str(e)}")
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
    campos_requeridos = ['nombre', 'apellido', 'fecha_de_nacimiento', 'telefono', 'direccion']

    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre = data['nombre']
        apellido = data['apellido']
        fecha_de_nacimiento = datetime.strptime(data['fecha_de_nacimiento'], '%Y-%m-%d')  # Asegúrate de validar el formato
        telefono = data['telefono']
        direccion = data['direccion']

        # Crear el objeto Estudiante con los datos proporcionados
        nuevo_estudiante = {
            'nombre': nombre,
            'apellido': apellido,
            'fecha_de_nacimiento': fecha_de_nacimiento,
            'telefono': telefono,
            'direccion': direccion
        }

        estudiante_id = estudiante_dao.guardarEstudiante(nuevo_estudiante)
        return jsonify({
            'success': True,
            'data': {'id_estudiante': estudiante_id, 'nombre': nombre, 'apellido': apellido},
            'error': None
        }), 201

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

    campos_requeridos = ['nombre', 'apellido', 'fecha_de_nacimiento', 'telefono', 'direccion']

    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    nombre = data['nombre']
    apellido = data['apellido']
    fecha_de_nacimiento = datetime.strptime(data['fecha_de_nacimiento'], '%Y-%m-%d')
    telefono = data['telefono']
    direccion = data['direccion']

    try:
        if estudiante_dao.updateEstudiante(estudiante_id, nombre, apellido, fecha_de_nacimiento, telefono, direccion):
            return jsonify({
                'success': True,
                'data': {'id_estudiante': estudiante_id, 'nombre': nombre, 'apellido': apellido},
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
