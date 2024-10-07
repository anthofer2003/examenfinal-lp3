from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.evaluacion.EvaluacionDao import EvaluacionDao

evaluacion_api = Blueprint('evaluacion_api', __name__)

# Trae todas las evaluaciones
@evaluacion_api.route('/evaluaciones', methods=['GET'])
def getEvaluaciones():
    evaluacion_dao = EvaluacionDao()

    try:
        evaluaciones = evaluacion_dao.getEvaluaciones()

        return jsonify({
            'success': True,
            'data': evaluaciones,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las evaluaciones: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@evaluacion_api.route('/evaluaciones/<int:evaluacion_id>', methods=['GET'])
def getEvaluacion(evaluacion_id):
    evaluacion_dao = EvaluacionDao()

    try:
        evaluacion = evaluacion_dao.getEvaluacionById(evaluacion_id)

        if evaluacion:
            return jsonify({
                'success': True,
                'data': evaluacion,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la evaluación con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener evaluación: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva evaluación
@evaluacion_api.route('/evaluaciones', methods=['POST'])
def addEvaluacion():
    data = request.get_json()
    evaluacion_dao = EvaluacionDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'tipo_evaluacion', 'fecha']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre = data['nombre']
        tipo_evaluacion = data['tipo_evaluacion']
        fecha = data['fecha']
        evaluacion_id = evaluacion_dao.guardarEvaluacion(nombre, tipo_evaluacion, fecha)
        if evaluacion_id:
            return jsonify({
                'success': True,
                'data': {'id': evaluacion_id, 'nombre': nombre, 'tipo_evaluacion': tipo_evaluacion, 'fecha': fecha},
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar la evaluación. Consulte con el administrador.'
            }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar evaluación: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@evaluacion_api.route('/evaluaciones/<int:evaluacion_id>', methods=['PUT'])
def updateEvaluacion(evaluacion_id):
    data = request.get_json()
    evaluacion_dao = EvaluacionDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'tipo_evaluacion', 'fecha']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    nombre = data['nombre']
    tipo_evaluacion = data['tipo_evaluacion']
    fecha = data['fecha']

    try:
        if evaluacion_dao.updateEvaluacion(evaluacion_id, nombre, tipo_evaluacion, fecha):
            return jsonify({
                'success': True,
                'data': {'id': evaluacion_id, 'nombre': nombre, 'tipo_evaluacion': tipo_evaluacion, 'fecha': fecha},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la evaluación con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar evaluación: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@evaluacion_api.route('/evaluaciones/<int:evaluacion_id>', methods=['DELETE'])
def deleteEvaluacion(evaluacion_id):
    evaluacion_dao = EvaluacionDao()

    try:
        # Usar el retorno de eliminarEvaluacion para determinar el éxito
        if evaluacion_dao.deleteEvaluacion(evaluacion_id):
            return jsonify({
                'success': True,
                'mensaje': f'La evaluación con ID {evaluacion_id} fue eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la evaluación con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar evaluación: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
