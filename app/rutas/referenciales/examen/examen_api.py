from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.examen.ExamenDao import TipoExamenDao

tipo_examen_api = Blueprint('tipo_examen_api', __name__)

# Trae todos los tipos de exámenes
@tipo_examen_api.route('/tipo_examenes', methods=['GET'])
def getTiposExamenes():
    tipo_examen_dao = TipoExamenDao()

    try:
        tipos_examen = tipo_examen_dao.getTiposExamenes()

        return jsonify({
            'success': True,
            'data': tipos_examen,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los tipos de exámenes: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipo_examen_api.route('/tipo_examenes/<int:tipo_examen_id>', methods=['GET'])
def getTipoExamen(tipo_examen_id):
    tipo_examen_dao = TipoExamenDao()

    try:
        tipo_examen = tipo_examen_dao.getTipoExamenById(tipo_examen_id)

        if tipo_examen:
            return jsonify({
                'success': True,
                'data': tipo_examen,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipo de examen con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener tipo de examen: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo tipo de examen
@tipo_examen_api.route('/tipo_examenes', methods=['POST'])
def addTipoExamen():
    data = request.get_json()
    tipo_examen_dao = TipoExamenDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        descripcion = data['descripcion'].upper()
        if tipo_examen_dao.guardarTipoExamen(descripcion):
            return jsonify({
                'success': True,
                'data': {'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar el tipo de examen. Consulte con el administrador.'
            }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar tipo de examen: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipo_examen_api.route('/tipo_examenes/<int:tipo_examen_id>', methods=['PUT'])
def updateTipoExamen(tipo_examen_id):
    data = request.get_json()
    tipo_examen_dao = TipoExamenDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    descripcion = data['descripcion']
    try:
        if tipo_examen_dao.updateTipoExamen(tipo_examen_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': tipo_examen_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipo de examen con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar tipo de examen: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipo_examen_api.route('/tipo_examenes/<int:tipo_examen_id>', methods=['DELETE'])
def deleteTipoExamen(tipo_examen_id):
    tipo_examen_dao = TipoExamenDao()

    try:
        # Usar el retorno de deleteTipoExamen para determinar el éxito
        if tipo_examen_dao.deleteTipoExamen(tipo_examen_id):
            return jsonify({
                'success': True,
                'mensaje': f'Tipo de examen con ID {tipo_examen_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipo de examen con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar tipo de examen: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
