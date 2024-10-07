from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.nacionalidad.NacionalidadDao import NacionalidadDao

nacioapi = Blueprint('nacioapi', __name__)

# Obtener todas las nacionalidades
@nacioapi.route('/nacionalidades', methods=['GET'])
def getNacionalidades():
    naciodao = NacionalidadDao()

    try:
        nacionalidades = naciodao.getNacionalidades()
        return jsonify({
            'success': True,
            'data': nacionalidades,
            'error': None
        }), 200
    except Exception as e:
        app.logger.error(f"Error al obtener todas las nacionalidades: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Obtener una nacionalidad por su ID
@nacioapi.route('/nacionalidades/<int:nacionalidad_id>', methods=['GET'])
def getNacionalidad(nacionalidad_id):
    naciodao = NacionalidadDao()

    try:
        nacionalidad = naciodao.getNacionalidadById(nacionalidad_id)
        if nacionalidad:
            return jsonify({
                'success': True,
                'data': nacionalidad,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la nacionalidad con el ID proporcionado.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al obtener nacionalidad: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agregar una nueva nacionalidad
@nacioapi.route('/nacionalidades', methods=['POST'])
def addNacionalidad():
    data = request.get_json()
    naciodao = NacionalidadDao()

    # Validar que los campos requeridos estén presentes
    campos_requeridos = ['nombre', 'apellido', 'nacionalidad']
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre = data['nombre'].strip().upper()
        apellido = data['apellido'].strip().upper()
        nacionalidad = data['nacionalidad'].strip().upper()

        if naciodao.guardarNacionalidad(nombre, apellido, nacionalidad):
            return jsonify({
                'success': True,
                'data': {'nombre': nombre, 'apellido': apellido, 'nacionalidad': nacionalidad},
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar la nacionalidad. Consulte con el administrador.'
            }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar nacionalidad: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Actualizar una nacionalidad por su ID
@nacioapi.route('/nacionalidades/<int:nacionalidad_id>', methods=['PUT'])
def updateNacionalidad(nacionalidad_id):
    data = request.get_json()
    naciodao = NacionalidadDao()

    # Validar que los campos requeridos estén presentes
    campos_requeridos = ['nombre', 'apellido', 'nacionalidad']
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre = data['nombre'].strip().upper()
        apellido = data['apellido'].strip().upper()
        nacionalidad = data['nacionalidad'].strip().upper()

        if naciodao.updateNacionalidad(nacionalidad_id, nombre, apellido, nacionalidad):
            return jsonify({
                'success': True,
                'data': {'id': nacionalidad_id, 'nombre': nombre, 'apellido': apellido, 'nacionalidad': nacionalidad},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la nacionalidad con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar nacionalidad: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Eliminar una nacionalidad por su ID
@nacioapi.route('/nacionalidades/<int:nacionalidad_id>', methods=['DELETE'])
def deleteNacionalidad(nacionalidad_id):
    naciodao = NacionalidadDao()

    try:
        if naciodao.deleteNacionalidad(nacionalidad_id):
            return jsonify({
                'success': True,
                'mensaje': f'Nacionalidad con ID {nacionalidad_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la nacionalidad con el ID proporcionado o no se pudo eliminar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al eliminar nacionalidad: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
