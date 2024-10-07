from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.nota.NotaDao import NotaDao

notaapi = Blueprint('notaapi', __name__)

# Trae todas las notas
@notaapi.route('/notas', methods=['GET'])
def getNotas():
    notaDao = NotaDao()
    
    try:
        notas = notaDao.getNotas()
        return jsonify({
            'success': True,
            'data': notas,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las notas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@notaapi.route('/notas/<int:nota_id>', methods=['GET'])
def getNota(nota_id):
    notaDao = NotaDao()

    try:
        nota = notaDao.getNotaById(nota_id)

        if nota:
            return jsonify({
                'success': True,
                'data': nota,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la nota con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener nota: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva nota
@notaapi.route('/notas', methods=['POST'])
def addNota():
    data = request.get_json()
    notaDao = NotaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre_estudiante', 'curso', 'nota', 'fecha_evaluacion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre_estudiante = data['nombre_estudiante']
        curso = data['curso']
        nota = data['nota']
        fecha_evaluacion = data['fecha_evaluacion']

        # Llamar a la función para guardar la nota
        if notaDao.guardarNota(nombre_estudiante, curso, nota, fecha_evaluacion):
            return jsonify({
                'success': True,
                'data': {
                    'nombre_estudiante': nombre_estudiante,
                    'curso': curso,
                    'nota': nota,
                    'fecha_evaluacion': fecha_evaluacion
                },
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar la nota. Consulte con el administrador.'
            }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar nota: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@notaapi.route('/notas/<int:nota_id>', methods=['PUT'])
def updateNota(nota_id):
    data = request.get_json()
    notaDao = NotaDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre_estudiante', 'curso', 'nota', 'fecha_evaluacion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    nombre_estudiante = data['nombre_estudiante']
    curso = data['curso']
    nota = data['nota']
    fecha_evaluacion = data['fecha_evaluacion']

    try:
        if notaDao.updateNota(nota_id, nombre_estudiante, curso, nota, fecha_evaluacion):
            return jsonify({
                'success': True,
                'data': {
                    'id': nota_id,
                    'nombre_estudiante': nombre_estudiante,
                    'curso': curso,
                    'nota': nota,
                    'fecha_evaluacion': fecha_evaluacion
                },
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la nota con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar nota: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@notaapi.route('/notas/<int:nota_id>', methods=['DELETE'])
def deleteNota(nota_id):
    notaDao = NotaDao()

    try:
        if notaDao.deleteNota(nota_id):
            return jsonify({
                'success': True,
                'mensaje': f'Nota con ID {nota_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la nota con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar nota: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
