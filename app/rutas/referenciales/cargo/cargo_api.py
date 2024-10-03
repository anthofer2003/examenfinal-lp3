from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.cargo.CargoDao import CargoDao

carapi = Blueprint('carapi', __name__)

# Trae todos los cargos
@carapi.route('/cargos', methods=['GET'])
def getCargos():
    cardao = CargoDao()

    try:
        cargos = cardao.getCargos()

        return jsonify({
            'success': True,
            'data': cargos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas los cargos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@carapi.route('/cargos/<int:cargo_id>', methods=['GET'])
def getCargo(cargo_id):
    cardao = CargoDao()

    try:
        cargo = cardao.getCargoById(cargo_id)

        if cargo:
            return jsonify({
                'success': True,
                'data': cargo,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el cargo con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener cargo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo cargo
@carapi.route('/cargos', methods=['POST'])
def addCargo():
    data = request.get_json()
    cardao = CargoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'apellido', 'numero_de_cedula', 'cargo']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        # Captura los datos
        nombre = data['nombre'].upper()
        apellido = data['apellido'].upper()
        numero_de_cedula = data['numero_de_cedula']
        cargo = data['cargo'].upper()

        # Guardar el nuevo cargo en la base de datos
        if cardao.guardarCargo(nombre, apellido, numero_de_cedula, cargo):
            return jsonify({
                'success': True,
                'data': {
                    'nombre': nombre,
                    'apellido': apellido,
                    'numero_de_cedula': numero_de_cedula,
                    'cargo': cargo
                },
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar el cargo. Consulte con el administrador.'
            }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar cargo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@carapi.route('/cargos/<int:cargo_id>', methods=['PUT'])
def updateCargo(cargo_id):
    data = request.get_json()
    cardao = CargoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'apellido', 'numero_de_cedula', 'cargo']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    nombre = data['nombre'].upper()
    apellido = data['apellido'].upper()
    numero_de_cedula = data['numero_de_cedula']
    cargo = data['cargo'].upper()

    try:
        if cardao.updateCargo(cargo_id, nombre, apellido, numero_de_cedula, cargo):
            return jsonify({
                'success': True,
                'data': {
                    'id': cargo_id,
                    'nombre': nombre,
                    'apellido': apellido,
                    'numero_de_cedula': numero_de_cedula,
                    'cargo': cargo
                },
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el cargo con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar cargo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@carapi.route('/cargos/<int:cargo_id>', methods=['DELETE'])
def deleteCargo(cargo_id):
    cardao = CargoDao()

    try:
        # Usar el retorno de eliminarCargo para determinar el éxito
        if cardao.deleteCargo(cargo_id):
            return jsonify({
                'success': True,
                'mensaje': f'Cargo con ID {cargo_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el cargo con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar cargo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
