from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.carrera.CarreraDao import CarreraDao

carrera_api = Blueprint('carrera_api', __name__)

# Trae todas las carreras
@carrera_api.route('/carreras', methods=['GET'])
def getCarreras():
    carrera_dao = CarreraDao()

    try:
        carreras = carrera_dao.getCarreras()

        return jsonify({
            'success': True,
            'data': carreras,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las carreras: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Trae una carrera por su ID
@carrera_api.route('/carreras/<int:carrera_id>', methods=['GET'])
def getCarrera(carrera_id):
    carrera_dao = CarreraDao()

    try:
        carrera = carrera_dao.getCarreraById(carrera_id)

        if carrera:
            return jsonify({
                'success': True,
                'data': carrera,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la carrera con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener la carrera: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva carrera
@carrera_api.route('/carreras', methods=['POST'])
def addCarrera():
    data = request.get_json()
    carrera_dao = CarreraDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'facultad_id', 'duracion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre = data['nombre'].upper()
        facultad_id = data['facultad_id']
        duracion = data['duracion']

        carrera_id = carrera_dao.guardarCarrera(nombre, facultad_id, duracion)
        if carrera_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': carrera_id, 'nombre': nombre, 'facultad_id': facultad_id, 'duracion': duracion},
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar la carrera. Consulte con el administrador.'
            }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar carrera: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Actualiza una carrera existente
@carrera_api.route('/carreras/<int:carrera_id>', methods=['PUT'])
def updateCarrera(carrera_id):
    data = request.get_json()
    carrera_dao = CarreraDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'facultad_id', 'duracion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    nombre = data['nombre'].upper()
    facultad_id = data['facultad_id']
    duracion = data['duracion']

    try:
        if carrera_dao.updateCarrera(carrera_id, nombre, facultad_id, duracion):
            return jsonify({
                'success': True,
                'data': {'id': carrera_id, 'nombre': nombre, 'facultad_id': facultad_id, 'duracion': duracion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la carrera con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar carrera: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Elimina una carrera
@carrera_api.route('/carreras/<int:carrera_id>', methods=['DELETE'])
def deleteCarrera(carrera_id):
    carrera_dao = CarreraDao()

    try:
        if carrera_dao.deleteCarrera(carrera_id):
            return jsonify({
                'success': True,
                'mensaje': f'Carrera con ID {carrera_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la carrera con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar carrera: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
