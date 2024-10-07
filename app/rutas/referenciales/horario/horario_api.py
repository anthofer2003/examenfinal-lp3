from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.horario.HorarioDao import HorarioDao


horarios_api = Blueprint('horarios_api', __name__)

# Obtener todos los horarios
@horarios_api.route('/horarios', methods=['GET'])
def getHorarios():
    horario_dao = HorarioDao()

    try:
        horarios = horario_dao.getHorarios()
        return jsonify({
            'success': True,
            'data': horarios,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener los horarios: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Obtener un horario por su ID
@horarios_api.route('/horarios/<int:horario_id>', methods=['GET'])
def getHorario(horario_id):
    horario_dao = HorarioDao()

    try:
        horario = horario_dao.getHorarioById(horario_id)

        if horario:
            return jsonify({
                'success': True,
                'data': horario,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el horario con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener el horario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agregar un nuevo horario
@horarios_api.route('/horarios', methods=['POST'])
def addHorario():
    data = request.get_json()
    horario_dao = HorarioDao()

    # Validar que el JSON contenga los campos necesarios
    campos_requeridos = ['curso', 'nombre_profesor', 'dia', 'hora_inicio', 'hora_fin', 'aula']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or not data[campo].strip():
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nuevo_horario = {
            'curso': data['curso'],
            'nombre_profesor': data['nombre_profesor'],
            'dia': data['dia'],
            'hora_inicio': data['hora_inicio'],
            'hora_fin': data['hora_fin'],
            'aula': data['aula']
        }

        horario_id = horario_dao.guardarHorario(nuevo_horario)
        if horario_id:
            return jsonify({
                'success': True,
                'data': {'id': horario_id, **nuevo_horario},
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar el horario. Consulte con el administrador.'
            }), 500

    except Exception as e:
        app.logger.error(f"Error al agregar el horario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Actualizar un horario existente
@horarios_api.route('/horarios/<int:horario_id>', methods=['PUT'])
def updateHorario(horario_id):
    data = request.get_json()
    horario_dao = HorarioDao()

    # Validar que el JSON contenga los campos necesarios
    campos_requeridos = ['curso', 'nombre_profesor', 'dia', 'hora_inicio', 'hora_fin', 'aula']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or not data[campo].strip():
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        horario_actualizado = {
            'curso': data['curso'],
            'nombre_profesor': data['nombre_profesor'],
            'dia': data['dia'],
            'hora_inicio': data['hora_inicio'],
            'hora_fin': data['hora_fin'],
            'aula': data['aula']
        }

        if horario_dao.updateHorario(horario_id, horario_actualizado):
            return jsonify({
                'success': True,
                'data': {'id': horario_id, **horario_actualizado},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el horario con el ID proporcionado o no se pudo actualizar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al actualizar el horario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Eliminar un horario
@horarios_api.route('/horarios/<int:horario_id>', methods=['DELETE'])
def deleteHorario(horario_id):
    horario_dao = HorarioDao()

    try:
        if horario_dao.deleteHorario(horario_id):
            return jsonify({
                'success': True,
                'mensaje': f'Horario con ID {horario_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el horario con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar el horario: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
