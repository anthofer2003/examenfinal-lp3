from flask import current_app as app
from app.conexion.Conexion import Conexion

class EstudianteDao:

    def getEstudiantes(self):
        estudianteSQL = """
        SELECT e.id_estudiante, e.curso
        FROM estudiante e
        JOIN personas p ON e.id_persona = p.id_persona
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(estudianteSQL)
            lista_estudiantes = cur.fetchall()
            lista_ordenada = []
            for item in lista_estudiantes:
                lista_ordenada.append({
                    "id_estudiante": item[0],
                    "curso": item[1],
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getEstudianteById(self, id_estudiante):
        estudianteSQL = """
        SELECT e.id_estudiante, e.curso
        FROM estudiante e
        JOIN personas p ON e.id_persona = p.id_persona
        WHERE e.id_estudiante = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(estudianteSQL, (id_estudiante,))
            estudianteEncontrado = cur.fetchone()
            if estudianteEncontrado:
                return {
                    "id_estudiante": estudianteEncontrado[0],
                    "curso": estudianteEncontrado[1],
                }
            return None
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarEstudiante(self, id_persona, curso):
        insertEstudianteSQL = """
        INSERT INTO estudiante (id_persona, curso)
        VALUES (%s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(insertEstudianteSQL, (id_persona, curso))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updateEstudiante(self, id_estudiante, curso):
        updateEstudianteSQL = """
        UPDATE estudiante
        SET curso = %s
        WHERE id_estudiante = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(updateEstudianteSQL, (curso, id_estudiante))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deleteEstudiante(self, id_estudiante):
        deleteEstudianteSQL = """
        DELETE FROM estudiante
        WHERE id_estudiante = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(deleteEstudianteSQL, (id_estudiante,))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
