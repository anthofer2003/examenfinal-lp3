from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.producto.ProductoDao import ProductoDao

producto_api = Blueprint('producto_api', __name__)

# Trae todos los productos
@producto_api.route('/productos', methods=['GET'])
def getProductos():
    producto_dao = ProductoDao()

    try:
        productos = producto_dao.getProductos()
        return jsonify({
            'success': True,
            'data': productos,
            'error': None
        }), 200
    except Exception as e:
        app.logger.error(f"Error al obtener todos los productos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Trae un producto por ID
@producto_api.route('/productos/<int:producto_id>', methods=['GET'])
def getProducto(producto_id):
    producto_dao = ProductoDao()

    try:
        producto = producto_dao.getProductoById(producto_id)
        if producto:
            return jsonify({
                'success': True,
                'data': producto,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el producto con el ID proporcionado.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al obtener producto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo producto
@producto_api.route('/productos', methods=['POST'])
def addProducto():
    data = request.get_json()
    producto_dao = ProductoDao()

    campos_requeridos = ['nombre_producto', 'precio', 'fecha_vencimiento']

    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre_producto = data['nombre_producto'].upper()
        precio = data['precio']
        fecha_vencimiento = data['fecha_vencimiento']

        producto_id = producto_dao.guardarProducto(nombre_producto, precio, fecha_vencimiento)
        return jsonify({
            'success': True,
            'data': {'id': producto_id, 'nombre_producto': nombre_producto, 'precio': precio, 'fecha_vencimiento': fecha_vencimiento},
            'error': None
        }), 201
    except Exception as e:
        app.logger.error(f"Error al agregar producto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Actualiza un producto
@producto_api.route('/productos/<int:producto_id>', methods=['PUT'])
def updateProducto(producto_id):
    data = request.get_json()
    producto_dao = ProductoDao()

    campos_requeridos = ['nombre_producto', 'precio', 'fecha_vencimiento']

    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre_producto = data['nombre_producto'].upper()
        precio = data['precio']
        fecha_vencimiento = data['fecha_vencimiento']

        if producto_dao.updateProducto(producto_id, nombre_producto, precio, fecha_vencimiento):
            return jsonify({
                'success': True,
                'data': {'id': producto_id, 'nombre_producto': nombre_producto, 'precio': precio, 'fecha_vencimiento': fecha_vencimiento},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo actualizar el producto.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar producto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Elimina un producto
@producto_api.route('/productos/<int:producto_id>', methods=['DELETE'])
def deleteProducto(producto_id):
    producto_dao = ProductoDao()

    try:
        if producto_dao.deleteProducto(producto_id):
            return jsonify({
                'success': True,
                'mensaje': f'Producto con ID {producto_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo eliminar el producto.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al eliminar producto: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
