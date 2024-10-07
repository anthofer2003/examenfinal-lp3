from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.matricula.MatriculaDao import MatriculaDao

matricula_api = Blueprint('matricula_api', __name__)

# Trae todas las matrículas
@matricula_api.route('/matriculas', methods=['GET'])
def getMatriculas():
    matriculadoao = MatriculaDao()

    try:
        matriculas = matriculadoao.getMatriculas()

        return jsonify({
            'success': True,
            'data': matriculas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las matrículas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@matricula_api.route('/matriculas/<int:matricula_id>', methods=['GET'])
def getMatricula(matricula_id):
    matriculadoao = MatriculaDao()

    try:
        matricula = matriculadoao.getMatriculaById(matricula_id)

        if matricula:
            return jsonify({
                'success': True,
                'data': matricula,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la matrícula con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener matrícula: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva matrícula
@matricula_api.route('/matriculas', methods=['POST'])
def addMatricula():
    data = request.get_json()
    matriculadoao = MatriculaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre_estudiante', 'curso', 'fecha_matricula', 'estado']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre_estudiante = data['nombre_estudiante'].upper()
        curso = data['curso'].upper()
        fecha_matricula = data['fecha_matricula']
        estado = data['estado'].upper()

        matricula_id = matriculadoao.guardarMatricula(nombre_estudiante, curso, fecha_matricula, estado)
        if matricula_id:
            return jsonify({
                'success': True,
                'data': {'id': matricula_id, 'nombre_estudiante': nombre_estudiante, 'curso': curso, 'fecha_matricula': fecha_matricula, 'estado': estado},
                'error': None
            }), 201
        else:
            return jsonify({'success': False, 'error': 'No se pudo guardar la matrícula. Consulte con el administrador.'}), 500
    except Exception as e:
        app.logger.error(f"Error al agregar matrícula: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@matricula_api.route('/matriculas/<int:matricula_id>', methods=['PUT'])
def updateMatricula(matricula_id):
    data = request.get_json()
    matriculadoao = MatriculaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre_estudiante', 'curso', 'fecha_matricula', 'estado']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    nombre_estudiante = data['nombre_estudiante'].upper()
    curso = data['curso'].upper()
    fecha_matricula = data['fecha_matricula']
    estado = data['estado'].upper()

    try:
        if matriculadoao.updateMatricula(matricula_id, nombre_estudiante, curso, fecha_matricula, estado):
            return jsonify({
                'success': True,
                'data': {'id': matricula_id, 'nombre_estudiante': nombre_estudiante, 'curso': curso, 'fecha_matricula': fecha_matricula, 'estado': estado},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la matrícula con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar matrícula: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@matricula_api.route('/matriculas/<int:matricula_id>', methods=['DELETE'])
def deleteMatricula(matricula_id):
    matriculadoao = MatriculaDao()

    try:
        if matriculadoao.deleteMatricula(matricula_id):
            return jsonify({
                'success': True,
                'mensaje': f'Matrícula con ID {matricula_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la matrícula con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar matrícula: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
