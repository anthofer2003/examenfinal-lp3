from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.persona.PersonaDao import PersonaDao

perapi = Blueprint('perapi', __name__)

# Trae todas las personas
@perapi.route('/personas', methods=['GET'])
def getPersonas():
    personadao = PersonaDao()
    try:
        personas = personadao.getPersonas()
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
@perapi.route('/personas/<int:persona_id>', methods=['GET'])
def getPersona(persona_id):
    personadao = PersonaDao()
    try:
        persona = personadao.getPersonaById(persona_id)
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
@perapi.route('/personas', methods=['POST'])
def addPersona():
    data = request.get_json()
    personadao = PersonaDao()

    campos_requeridos = ['nombre', 'apellido', 'numero_de_cedula']
    for campo in campos_requeridos:
        if campo not in data or not data[campo].strip():
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre = data['nombre'].strip()
        apellido = data['apellido'].strip()
        numero_de_cedula = data['numero_de_cedula'].strip()

        persona_id = personadao.guardarPersona(nombre, apellido, numero_de_cedula)
        if persona_id:
            return jsonify({
                'success': True,
                'data': {'id': persona_id, 'nombre': nombre, 'apellido': apellido, 'numero_de_cedula': numero_de_cedula},
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

# Actualiza una persona por ID
@perapi.route('/personas/<int:persona_id>', methods=['PUT'])
def updatePersona(persona_id):
    data = request.get_json()
    personadao = PersonaDao()

    campos_requeridos = ['nombre', 'apellido', 'numero_de_cedula']
    for campo in campos_requeridos:
        if campo not in data or not data[campo].strip():
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre = data['nombre'].strip()
        apellido = data['apellido'].strip()
        numero_de_cedula = data['numero_de_cedula'].strip()

        if personadao.updatePersona(persona_id, nombre, apellido, numero_de_cedula):
            return jsonify({
                'success': True,
                'data': {'id': persona_id, 'nombre': nombre, 'apellido': apellido, 'numero_de_cedula': numero_de_cedula},
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

# Elimina una persona por ID
@perapi.route('/personas/<int:persona_id>', methods=['DELETE'])
def deletePersona(persona_id):
    personadao = PersonaDao()
    try:
        if personadao.deletePersona(persona_id):
            return jsonify({
                'success': True,
                'mensaje': f'Persona con ID {persona_id} eliminada correctamente.',
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