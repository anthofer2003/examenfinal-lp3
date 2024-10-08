from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.programa.ProgramaDao import ProgramaDao

programa_api = Blueprint('programa_api', __name__)

# Trae todos los programas
@programa_api.route('/programas', methods=['GET'])
def getProgramas():
    programa_dao = ProgramaDao()

    try:
        programas = programa_dao.getProgramas()

        return jsonify({
            'success': True,
            'data': programas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los programas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@programa_api.route('/programas/<int:programa_id>', methods=['GET'])
def getPrograma(programa_id):
    programa_dao = ProgramaDao()

    try:
        programa = programa_dao.getProgramaById(programa_id)

        if programa:
            return jsonify({
                'success': True,
                'data': programa,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el programa con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener programa: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo programa
@programa_api.route('/programas', methods=['POST'])
def addPrograma():
    data = request.get_json()
    programa_dao = ProgramaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'facultad', 'duracion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre = data['nombre'].upper()
        facultad = data['facultad'].upper()
        duracion = data['duracion']

        if not isinstance(duracion, int) or duracion <= 0:
            return jsonify({
                'success': False,
                'error': 'La duración debe ser un número entero positivo.'
            }), 400

        programa_id = programa_dao.guardarPrograma(nombre, facultad, duracion)
        if programa_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': programa_id, 'nombre': nombre, 'facultad': facultad, 'duracion': duracion},
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar el programa. Consulte con el administrador.'
            }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar programa: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@programa_api.route('/programas/<int:programa_id>', methods=['PUT'])
def updatePrograma(programa_id):
    data = request.get_json()
    programa_dao = ProgramaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'facultad', 'duracion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    nombre = data['nombre'].upper()
    facultad = data['facultad'].upper()
    duracion = data['duracion']

    if not isinstance(duracion, int) or duracion <= 0:
        return jsonify({
            'success': False,
            'error': 'La duración debe ser un número entero positivo.'
        }), 400

    try:
        if programa_dao.updatePrograma(programa_id, nombre, facultad, duracion):
            return jsonify({
                'success': True,
                'data': {'id': programa_id, 'nombre': nombre, 'facultad': facultad, 'duracion': duracion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el programa con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar programa: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@programa_api.route('/programas/<int:programa_id>', methods=['DELETE'])
def deletePrograma(programa_id):
    programa_dao = ProgramaDao()

    try:
        if programa_dao.deletePrograma(programa_id):
            return jsonify({
                'success': True,
                'mensaje': f'Programa con ID {programa_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el programa con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar programa: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
