# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class NacionalidadDao:

    def getNacionalidades(self):
        nacionalidadSQL = """
        SELECT id, nombre, apellido, nacionalidad
        FROM nacionalidades
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(nacionalidadSQL)
            lista_nacionalidades = cur.fetchall()
            lista_ordenada = []
            for item in lista_nacionalidades:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "apellido": item[2],
                    "nacionalidad": item[3]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getNacionalidadById(self, id):
        nacionalidadSQL = """
        SELECT id, nombre, apellido, nacionalidad
        FROM nacionalidades
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(nacionalidadSQL, (id,))
            nacionalidadEncontrada = cur.fetchone()
            if nacionalidadEncontrada:
                return {
                    "id": nacionalidadEncontrada[0],
                    "nombre": nacionalidadEncontrada[1],
                    "apellido": nacionalidadEncontrada[2],
                    "nacionalidad": nacionalidadEncontrada[3]
                }
            else:
                return None
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarNacionalidad(self, nombre, apellido, nacionalidad):
        insertNacionalidadSQL = """
        INSERT INTO nacionalidades(nombre, apellido, nacionalidad) 
        VALUES(%s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(insertNacionalidadSQL, (nombre, apellido, nacionalidad))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()
        return False

    def updateNacionalidad(self, id, nombre, apellido, nacionalidad):
        updateNacionalidadSQL = """
        UPDATE nacionalidades
        SET nombre=%s, apellido=%s, nacionalidad=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(updateNacionalidadSQL, (nombre, apellido, nacionalidad, id))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()
        return False

    def deleteNacionalidad(self, id):
        deleteNacionalidadSQL = """
        DELETE FROM nacionalidades
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(deleteNacionalidadSQL, (id,))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()
        return False
