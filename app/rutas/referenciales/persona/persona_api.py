from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.persona.PersonaDao import PersonaDao
from datetime import datetime

persona_api = Blueprint('persona_api', __name__)

# Trae todas las personas
@persona_api.route('/personas', methods=['GET'])
def getPersonas():
    persona_dao = PersonaDao()
    try:
        personas = persona_dao.getPersonas()
        return jsonify({
            'success': True,
            'data': personas,
            'error': None
        }), 200
    except Exception as e:
        app.logger.error(f"Error al obtener todas las personas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Trae una persona por ID
@persona_api.route('/personas/<int:id_persona>', methods=['GET'])
def getPersona(id_persona):
    persona_dao = PersonaDao()
    try:
        persona = persona_dao.getPersonaById(id_persona)
        if persona:
            return jsonify({
                'success': True,
                'data': persona,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la persona con el ID proporcionado.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al obtener persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva persona
@persona_api.route('/personas', methods=['POST'])
def addPersona():
    data = request.get_json()
    persona_dao = PersonaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombres', 'apellidos', 'ci', 'fechanac', 'creacion_usuario']

    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        # Obtiene la fecha y hora de creación
        creacion_fecha = datetime.now().date()
        creacion_hora = datetime.now().time()

        id_persona = persona_dao.guardarPersona(
            data['nombres'],
            data['apellidos'],
            data['ci'],
            data['fechanac'],
            creacion_fecha,
            creacion_hora,
            data['creacion_usuario']
        )
        if id_persona:
            return jsonify({
                'success': True,
                'data': {'id_persona': id_persona},
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar la persona. Consulte con el administrador.'
            }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Actualiza una persona existente
@persona_api.route('/personas/<int:id_persona>', methods=['PUT'])
def updatePersona(id_persona):
    data = request.get_json()
    persona_dao = PersonaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombres', 'apellidos', 'ci', 'fechanac']

    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        if persona_dao.updatePersona(
            id_persona,
            data['nombres'],
            data['apellidos'],
            data['ci'],
            data['fechanac']
        ):
            return jsonify({
                'success': True,
                'data': {'id_persona': id_persona},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la persona con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Elimina una persona
@persona_api.route('/personas/<int:id_persona>', methods=['DELETE'])
def deletePersona(id_persona):
    persona_dao = PersonaDao()
    try:
        if persona_dao.deletePersona(id_persona):
            return jsonify({
                'success': True,
                'mensaje': f'Persona con ID {id_persona} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la persona con el ID proporcionado o no se pudo eliminar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al eliminar persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
