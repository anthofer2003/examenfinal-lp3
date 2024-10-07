# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class EvaluacionDao:

    def getEvaluaciones(self):
        evaluacionSQL = """
        SELECT id, nombre, tipo_evaluacion, fecha
        FROM evaluaciones
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(evaluacionSQL)
            # trae datos de la bd
            lista_evaluaciones = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_evaluaciones:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "tipo_evaluacion": item[2],
                    "fecha": item[3]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getEvaluacionById(self, id):
        evaluacionSQL = """
        SELECT id, nombre, tipo_evaluacion, fecha
        FROM evaluaciones WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(evaluacionSQL, (id,))
            # trae datos de la bd
            evaluacionEncontrada = cur.fetchone()
            # retorno los datos
            return {
                "id": evaluacionEncontrada[0],
                "nombre": evaluacionEncontrada[1],
                "tipo_evaluacion": evaluacionEncontrada[2],
                "fecha": evaluacionEncontrada[3]
            }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarEvaluacion(self, nombre, tipo_evaluacion, fecha):
        insertEvaluacionSQL = """
        INSERT INTO evaluaciones(nombre, tipo_evaluacion, fecha) VALUES(%s, %s, %s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertEvaluacionSQL, (nombre, tipo_evaluacion, fecha))
            # se confirma la insercion
            con.commit()
            return True

        # Si algo fallo entra aquí
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va a ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def updateEvaluacion(self, id, nombre, tipo_evaluacion, fecha):
        updateEvaluacionSQL = """
        UPDATE evaluaciones
        SET nombre=%s, tipo_evaluacion=%s, fecha=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateEvaluacionSQL, (nombre, tipo_evaluacion, fecha, id))
            # se confirma la insercion
            con.commit()
            return True

        # Si algo fallo entra aquí
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va a ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def deleteEvaluacion(self, id):
        deleteEvaluacionSQL = """
        DELETE FROM evaluaciones
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteEvaluacionSQL, (id,))
            # se confirma la insercion
            con.commit()
            return True

        # Si algo fallo entra aquí
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va a ejecutar
        finally:
            cur.close()
            con.close()

        return False
