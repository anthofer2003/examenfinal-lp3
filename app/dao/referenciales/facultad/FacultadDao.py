# Data Access Object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class FacultadDao:

    def getFacultades(self):
        facultadSQL = """
        SELECT id, nombre, ubicacion
        FROM facultades
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(facultadSQL)
            # Traer datos de la BD
            lista_facultades = cur.fetchall()
            # Formatear los datos
            lista_ordenada = []
            for item in lista_facultades:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "ubicacion": item[2]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getFacultadById(self, id):
        facultadSQL = """
        SELECT id, nombre, ubicacion
        FROM facultades
        WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(facultadSQL, (id,))
            # Obtener la facultad
            facultad_encontrada = cur.fetchone()
            # Verificar si se encontró la facultad
            if facultad_encontrada:
                return {
                    "id": facultad_encontrada[0],
                    "nombre": facultad_encontrada[1],
                    "ubicacion": facultad_encontrada[2]
                }
            else:
                return None
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarFacultad(self, nombre, ubicacion):
        insertFacultadSQL = """
        INSERT INTO facultades (nombre, ubicacion)
        VALUES (%s, %s)
        RETURNING id
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(insertFacultadSQL, (nombre, ubicacion))
            # Confirmar la inserción
            con.commit()
            # Obtener el ID generado
            facultad_id = cur.fetchone()[0]
            return facultad_id
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return None

    def updateFacultad(self, id, nombre, ubicacion):
        updateFacultadSQL = """
        UPDATE facultades
        SET nombre = %s, ubicacion = %s
        WHERE id = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateFacultadSQL, (nombre, ubicacion, id))
            # Confirmar la actualización
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deleteFacultad(self, id):
        deleteFacultadSQL = """
        DELETE FROM facultades
        WHERE id = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteFacultadSQL, (id,))
            # Confirmar la eliminación
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
