from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.profesor.ProfesorDao import ProfesorDao

profesorapi = Blueprint('profesorapi', __name__)

# Trae todos los profesores
@profesorapi.route('/profesores', methods=['GET'])
def getProfesores():
    profesordao = ProfesorDao()
    try:
        profesores = profesordao.getProfesores()
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

# Trae un profesor específico
@profesorapi.route('/profesores/<int:id_profesor>', methods=['GET'])
def getProfesor(id_profesor):
    profesordao = ProfesorDao()
    try:
        profesor = profesordao.getProfesorById(id_profesor)
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
@profesorapi.route('/profesores', methods=['POST'])
def addProfesor():
    data = request.get_json()
    profesordao = ProfesorDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre_profesor', 'apellido_profesor', 'titulo_academico', 'correo', 'telefono']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre_profesor = data['nombre_profesor']
        apellido_profesor = data['apellido_profesor']
        titulo_academico = data['titulo_academico']
        correo = data['correo']
        telefono = data['telefono']
        
        if profesordao.guardarProfesor(nombre_profesor, apellido_profesor, titulo_academico, correo, telefono):
            return jsonify({
                'success': True,
                'data': {'nombre_profesor': nombre_profesor, 'apellido_profesor': apellido_profesor},
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

# Actualiza un profesor existente
@profesorapi.route('/profesores/<int:id_profesor>', methods=['PUT'])
def updateProfesor(id_profesor):
    data = request.get_json()
    profesordao = ProfesorDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre_profesor', 'apellido_profesor', 'titulo_academico', 'correo', 'telefono']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400
            
    nombre_profesor = data['nombre_profesor']
    apellido_profesor = data['apellido_profesor']
    titulo_academico = data['titulo_academico']
    correo = data['correo']
    telefono = data['telefono']

    try:
        if profesordao.updateProfesor(id_profesor, nombre_profesor, apellido_profesor, titulo_academico, correo, telefono):
            return jsonify({
                'success': True,
                'data': {'id_profesor': id_profesor, 'nombre_profesor': nombre_profesor},
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

# Elimina un profesor
@profesorapi.route('/profesores/<int:id_profesor>', methods=['DELETE'])
def deleteProfesor(id_profesor):
    profesordao = ProfesorDao()

    try:
        if profesordao.deleteProfesor(id_profesor):
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
