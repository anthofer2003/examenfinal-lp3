# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class NacionalidadDao:

    def getNacionalidades(self):

        nacionalidadSQL = """
        SELECT id, descripcion
        FROM nacionalidades
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(nacionalidadSQL)
            # trae datos de la bd
            lista_nacionalidades = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_nacionalidades:
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

    def getNacionalidadById(self, id):

        nacionalidadSQL = """
        SELECT id, descripcion
        FROM nacionalidades WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(nacionalidadSQL, (id,))
            # trae datos de la bd
            nacionalidadEncontrada = cur.fetchone()
            # retorno los datos
            return {
                    "id": nacionalidadEncontrada[0],
                    "descripcion": nacionalidadEncontrada[1]
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarNacionalidad(self, descripcion):

        insertNacionalidadSQL = """
        INSERT INTO nacionalidades(descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertNacionalidadSQL, (descripcion,))
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

    def updateNacionalidad(self, id, descripcion):

        updateNacionalidadSQL = """
        UPDATE nacionalidades
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateNacionalidadSQL, (descripcion, id,))
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

    def deleteNacionalidad(self, id):

        updateNacionalidadSQL = """
        DELETE FROM nacionalidades
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateNacionalidadSQL, (id,))
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