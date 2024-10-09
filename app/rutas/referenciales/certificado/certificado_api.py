from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.certificado.CertificadoDao import TipoCertificadoDao

tipocertificado_api = Blueprint('tipocertificado_api', __name__)

# Trae todos los tipos de certificados
@tipocertificado_api.route('/tipo_certificados', methods=['GET'])
def getTiposCertificados():
    tipocertificado_dao = TipoCertificadoDao()

    try:
        tipos_certificados = tipocertificado_dao.getTiposCertificados()

        return jsonify({
            'success': True,
            'data': tipos_certificados,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los tipos de certificados: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipocertificado_api.route('/tipo_certificados/<int:tipo_certificado_id>', methods=['GET'])
def getTipoCertificado(tipo_certificado_id):
    tipocertificado_dao = TipoCertificadoDao()

    try:
        tipo_certificado = tipocertificado_dao.getTipoCertificadoById(tipo_certificado_id)

        if tipo_certificado:
            return jsonify({
                'success': True,
                'data': tipo_certificado,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipo de certificado con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener tipo de certificado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo tipo de certificado
@tipocertificado_api.route('/tipo_certificados', methods=['POST'])
def addTipoCertificado():
    data = request.get_json()
    tipocertificado_dao = TipoCertificadoDao()

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
        tipo_certificado_id = tipocertificado_dao.guardarTipoCertificado(descripcion)
        if tipo_certificado_id:
            return jsonify({
                'success': True,
                'data': {'id': tipo_certificado_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar el tipo de certificado. Consulte con el administrador.'
            }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar tipo de certificado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipocertificado_api.route('/tipo_certificados/<int:tipo_certificado_id>', methods=['PUT'])
def updateTipoCertificado(tipo_certificado_id):
    data = request.get_json()
    tipocertificado_dao = TipoCertificadoDao()

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
        if tipocertificado_dao.updateTipoCertificado(tipo_certificado_id, descripcion.upper()):
            return jsonify({
                'success': True,
                'data': {'id': tipo_certificado_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipo de certificado con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar tipo de certificado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@tipocertificado_api.route('/tipo_certificados/<int:tipo_certificado_id>', methods=['DELETE'])
def deleteTipoCertificado(tipo_certificado_id):
    tipocertificado_dao = TipoCertificadoDao()

    try:
        # Usar el retorno de eliminarTipoCertificado para determinar el éxito
        if tipocertificado_dao.deleteTipoCertificado(tipo_certificado_id):
            return jsonify({
                'success': True,
                'mensaje': f'Tipo de certificado con ID {tipo_certificado_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el tipo de certificado con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar tipo de certificado: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
