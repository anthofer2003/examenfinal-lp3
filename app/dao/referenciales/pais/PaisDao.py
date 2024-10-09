# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class PaisDao:

    def getPaises(self):
        paisSQL = """
        SELECT id, descripcion
        FROM paises
        """
        # Objeto conexión
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(paisSQL)
            # Trae datos de la BD
            lista_paises = cur.fetchall()
            # Retorno los datos
            lista_ordenada = []
            for item in lista_paises:
                lista_ordenada.append({
                    "id": item[0],
                    "descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getPaisById(self, id):
        paisSQL = """
        SELECT id, descripcion
        FROM paises WHERE id=%s
        """
        # Objeto conexión
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(paisSQL, (id,))
            # Trae el dato de la BD
            paisEncontrado = cur.fetchone()
            # Retorno el dato
            return {
                    "id": paisEncontrado[0],
                    "descripcion": paisEncontrado[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarPais(self, descripcion):
        insertPaisSQL = """
        INSERT INTO paises(descripcion) VALUES(%s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecución exitosa
        try:
            cur.execute(insertPaisSQL, (descripcion,))
            # Confirma la inserción
            con.commit()

            return True

        # Si algo falló entra aquí
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def updatePais(self, id, descripcion):
        updatePaisSQL = """
        UPDATE paises
        SET descripcion=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecución exitosa
        try:
            cur.execute(updatePaisSQL, (descripcion, id,))
            # Confirma la actualización
            con.commit()

            return True

        # Si algo falló entra aquí
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def deletePais(self, id):
        deletePaisSQL = """
        DELETE FROM paises
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecución exitosa
        try:
            cur.execute(deletePaisSQL, (id,))
            # Confirma la eliminación
            con.commit()

            return True

        # Si algo falló entra aquí
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False
