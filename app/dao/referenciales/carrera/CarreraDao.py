# Data Access Object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class CarreraDao:

    def getCarreras(self):
        carreraSQL = """
        SELECT id, nombre, facultad_id, duracion
        FROM carreras
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(carreraSQL)
            # Traer datos de la BD
            lista_carreras = cur.fetchall()
            # Formatear los datos
            lista_ordenada = []
            for item in lista_carreras:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "facultad_id": item[2],
                    "duracion": item[3]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getCarreraById(self, id):
        carreraSQL = """
        SELECT id, nombre, facultad_id, duracion
        FROM carreras
        WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(carreraSQL, (id,))
            # Obtener la carrera
            carrera_encontrada = cur.fetchone()
            # Verificar si se encontró la carrera
            if carrera_encontrada:
                return {
                    "id": carrera_encontrada[0],
                    "nombre": carrera_encontrada[1],
                    "facultad_id": carrera_encontrada[2],
                    "duracion": carrera_encontrada[3]
                }
            else:
                return None
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarCarrera(self, nombre, facultad_id, duracion):
        insertCarreraSQL = """
        INSERT INTO carreras (nombre, facultad_id, duracion)
        VALUES (%s, %s, %s)
        RETURNING id
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(insertCarreraSQL, (nombre, facultad_id, duracion))
            # Confirmar la inserción
            con.commit()
            # Obtener el ID generado
            carrera_id = cur.fetchone()[0]
            return carrera_id
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return None

    def updateCarrera(self, id, nombre, facultad_id, duracion):
        updateCarreraSQL = """
        UPDATE carreras
        SET nombre = %s, facultad_id = %s, duracion = %s
        WHERE id = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateCarreraSQL, (nombre, facultad_id, duracion, id))
            # Confirmar la actualización
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deleteCarrera(self, id):
        deleteCarreraSQL = """
        DELETE FROM carreras
        WHERE id = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteCarreraSQL, (id,))
            # Confirmar la eliminación
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
