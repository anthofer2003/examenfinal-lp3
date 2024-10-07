# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class NotaDao:

    def getNotas(self):
        notasSQL = """
        SELECT id, nombre_estudiante, curso, nota, fecha_evaluacion
        FROM notas
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(notasSQL)
            # trae datos de la bd
            lista_notas = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_notas:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre_estudiante": item[1],
                    "curso": item[2],
                    "nota": item[3],
                    "fecha_evaluacion": item[4].isoformat()  # Convertir a formato ISO
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getNotaById(self, id):
        notaSQL = """
        SELECT id, nombre_estudiante, curso, nota, fecha_evaluacion
        FROM notas WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(notaSQL, (id,))
            # trae datos de la bd
            notaEncontrada = cur.fetchone()
            # retorno los datos
            return {
                    "id": notaEncontrada[0],
                    "nombre_estudiante": notaEncontrada[1],
                    "curso": notaEncontrada[2],
                    "nota": notaEncontrada[3],
                    "fecha_evaluacion": notaEncontrada[4].isoformat()  # Convertir a formato ISO
                }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarNota(self, nombre_estudiante, curso, nota, fecha_evaluacion):
        insertNotaSQL = """
        INSERT INTO notas(nombre_estudiante, curso, nota, fecha_evaluacion) VALUES(%s, %s, %s, %s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertNotaSQL, (nombre_estudiante, curso, nota, fecha_evaluacion))
            # se confirma la insercion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updateNota(self, id, nombre_estudiante, curso, nota, fecha_evaluacion):
        updateNotaSQL = """
        UPDATE notas
        SET nombre_estudiante=%s, curso=%s, nota=%s, fecha_evaluacion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateNotaSQL, (nombre_estudiante, curso, nota, fecha_evaluacion, id))
            # se confirma la insercion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deleteNota(self, id):
        deleteNotaSQL = """
        DELETE FROM notas
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteNotaSQL, (id,))
            # se confirma la insercion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
