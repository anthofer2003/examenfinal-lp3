from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.pais.PaisDao import PaisDao

paiapi = Blueprint('paiapi', __name__)

# Trae todas las países
@paiapi.route('/paises', methods=['GET'])
def getPaises():
    paidao = PaisDao()

    try:
        paises = paidao.getPaises()

        return jsonify({
            'success': True,
            'data': paises,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las países: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@paiapi.route('/paises/<int:pais_id>', methods=['GET'])
def getPais(pais_id):
    paidao = PaisDao()

    try:
        pais = paidao.getPaisById(pais_id)

        if pais:
            return jsonify({
                'success': True,
                'data': pais,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el país con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener país: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo país
@paiapi.route('/paises', methods=['POST'])
def addPais():
    data = request.get_json()
    paidao = PaisDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'apellido', 'pais']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        nombre = data['nombre'].upper()
        apellido = data['apellido'].upper()
        pais = data['pais'].upper()

        pais_id = paidao.guardarPais(nombre, apellido, pais)
        if pais_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': pais_id, 'nombre': nombre, 'apellido': apellido, 'pais': pais},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el país. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar país: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@paiapi.route('/paises/<int:pais_id>', methods=['PUT'])
def updatePais(pais_id):
    data = request.get_json()
    paidao = PaisDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'apellido', 'pais']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    nombre = data['nombre']
    apellido = data['apellido']
    pais = data['pais']
    try:
        if paidao.updatePais(pais_id, nombre.upper(), apellido.upper(), pais.upper()):
            return jsonify({
                'success': True,
                'data': {'id': pais_id, 'nombre': nombre, 'apellido': apellido, 'pais': pais},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el país con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar país: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@paiapi.route('/paises/<int:pais_id>', methods=['DELETE'])
def deletePais(pais_id):
    paidao = PaisDao()

    try:
        if paidao.deletePais(pais_id):
            return jsonify({
                'success': True,
                'mensaje': f'País con ID {pais_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el país con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar país: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
