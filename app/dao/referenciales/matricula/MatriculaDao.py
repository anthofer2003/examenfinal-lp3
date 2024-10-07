# Data Access Object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class MatriculaDao:

    def getMatriculas(self):
        matriculaSQL = """
        SELECT id, nombre_estudiante, curso, fecha_matricula, estado
        FROM matriculas
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(matriculaSQL)
            # trae datos de la bd
            lista_matriculas = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_matriculas:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre_estudiante": item[1],
                    "curso": item[2],
                    "fecha_matricula": item[3],
                    "estado": item[4]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getMatriculaById(self, id):
        matriculaSQL = """
        SELECT id, nombre_estudiante, curso, fecha_matricula, estado
        FROM matriculas WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(matriculaSQL, (id,))
            # trae datos de la bd
            matriculaEncontrada = cur.fetchone()
            # retorno los datos
            return {
                "id": matriculaEncontrada[0],
                "nombre_estudiante": matriculaEncontrada[1],
                "curso": matriculaEncontrada[2],
                "fecha_matricula": matriculaEncontrada[3],
                "estado": matriculaEncontrada[4]
            }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarMatricula(self, nombre_estudiante, curso, fecha_matricula, estado):
        insertMatriculaSQL = """
        INSERT INTO matriculas(nombre_estudiante, curso, fecha_matricula, estado) VALUES(%s, %s, %s, %s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertMatriculaSQL, (nombre_estudiante, curso, fecha_matricula, estado))
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

    def updateMatricula(self, id, nombre_estudiante, curso, fecha_matricula, estado):
        updateMatriculaSQL = """
        UPDATE matriculas
        SET nombre_estudiante=%s, curso=%s, fecha_matricula=%s, estado=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateMatriculaSQL, (nombre_estudiante, curso, fecha_matricula, estado, id))
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

    def deleteMatricula(self, id):
        deleteMatriculaSQL = """
        DELETE FROM matriculas
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteMatriculaSQL, (id,))
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
