from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.curso.CursoDao import CursoParticularDao

cursos_api = Blueprint('cursos_api', __name__)

# Obtener todos los cursos
@cursos_api.route('/cursos', methods=['GET'])
def getCursos():
    curso_dao = CursoParticularDao()

    try:
        cursos = curso_dao.getCursosParticulares()
        return jsonify({
            'success': True,
            'data': cursos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener los cursos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Obtener un curso por su ID
@cursos_api.route('/cursos/<int:curso_id>', methods=['GET'])
def getCurso(curso_id):
    curso_dao = CursoParticularDao()

    try:
        curso = curso_dao.getCursoParticularById(curso_id)

        if curso:
            return jsonify({
                'success': True,
                'data': curso,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el curso con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener el curso: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agregar un nuevo curso
@cursos_api.route('/cursos', methods=['POST'])
def addCurso():
    data = request.get_json()
    curso_dao = CursoParticularDao()

    # Validar que el JSON contenga los campos necesarios
    campos_requeridos = ['curso', 'fecha_inicio', 'fecha_fin', 'precio_mes']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or not data[campo].strip():
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        curso_id = curso_dao.guardarCursoParticular(data['curso'], data['fecha_inicio'], data['fecha_fin'], data['precio_mes'])
        if curso_id:
            return jsonify({
                'success': True,
                'data': {'id': curso_id, **data},
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar el curso. Consulte con el administrador.'
            }), 500

    except Exception as e:
        app.logger.error(f"Error al agregar el curso: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Actualizar un curso existente
@cursos_api.route('/cursos/<int:curso_id>', methods=['PUT'])
def updateCurso(curso_id):
    data = request.get_json()
    curso_dao = CursoParticularDao()

    # Validar que el JSON contenga los campos necesarios
    campos_requeridos = ['curso', 'fecha_inicio', 'fecha_fin', 'precio_mes']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or not data[campo].strip():
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        if curso_dao.updateCursoParticular(curso_id, data['curso'], data['fecha_inicio'], data['fecha_fin'], data['precio_mes']):
            return jsonify({
                'success': True,
                'data': {'id': curso_id, **data},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el curso con el ID proporcionado o no se pudo actualizar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al actualizar el curso: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Eliminar un curso
@cursos_api.route('/cursos/<int:curso_id>', methods=['DELETE'])
def deleteCurso(curso_id):
    curso_dao = CursoParticularDao()

    try:
        if curso_dao.deleteCursoParticular(curso_id):
            return jsonify({
                'success': True,
                'mensaje': f'Curso con ID {curso_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el curso con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar el curso: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
