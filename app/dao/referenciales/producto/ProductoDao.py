# Data Access Object - DAO para la tabla productos
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ProductoDao:

    def getProductos(self):
        productoSQL = """
        SELECT id, nombre_producto, precio, fecha_vencimiento
        FROM productos
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(productoSQL)
            # trae datos de la bd
            lista_productos = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_productos:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre_producto": item[1],
                    "precio": item[2],
                    "fecha_vencimiento": item[3]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getProductoById(self, id):
        productoSQL = """
        SELECT id, nombre_producto, precio, fecha_vencimiento
        FROM productos WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(productoSQL, (id,))
            # trae datos de la bd
            productoEncontrado = cur.fetchone()
            # retorno los datos
            return {
                "id": productoEncontrado[0],
                "nombre_producto": productoEncontrado[1],
                "precio": productoEncontrado[2],
                "fecha_vencimiento": productoEncontrado[3]
            }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarProducto(self, nombre_producto, precio, fecha_vencimiento):
        insertProductoSQL = """
        INSERT INTO productos(nombre_producto, precio, fecha_vencimiento) 
        VALUES(%s, %s, %s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertProductoSQL, (nombre_producto, precio, fecha_vencimiento))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def updateProducto(self, id, nombre_producto, precio, fecha_vencimiento):
        updateProductoSQL = """
        UPDATE productos
        SET nombre_producto=%s, precio=%s, fecha_vencimiento=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateProductoSQL, (nombre_producto, precio, fecha_vencimiento, id))
            # se confirma la actualizacion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def deleteProducto(self, id):
        deleteProductoSQL = """
        DELETE FROM productos
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteProductoSQL, (id,))
            # se confirma la eliminacion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False
