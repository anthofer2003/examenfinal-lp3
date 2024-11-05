# Data access object - DAO para Profesor
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ProfesorDao:

    def getProfesores(self):
        profesorSQL = """
        SELECT p.id_profesor, p.asignatura, p.salario
        FROM profesor p
        JOIN persona per ON p.id_persona = per.id_persona
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(profesorSQL)
            lista_profesores = cur.fetchall()
            lista_ordenada = []
            for item in lista_profesores:
                lista_ordenada.append({
                    "id_profesor": item[0],
                    "asignatura": item[1],
                    "salario": item[2]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getProfesorById(self, id_profesor):
        profesorSQL = """
        SELECT p.id_profesor, p.asignatura, p.salario
        FROM profesor p
        JOIN persona per ON p.id_persona = per.id_persona
        WHERE p.id_profesor=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(profesorSQL, (id_profesor,))
            profesorEncontrado = cur.fetchone()
            return {
                "id_profesor": profesorEncontrado[0],
                "asignatura": profesorEncontrado[1],
                "salario": profesorEncontrado[2]
            }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarProfesor(self, id_persona, asignatura, salario):
        insertProfesorSQL = """
        INSERT INTO profesor(id_persona, asignatura, salario) 
        VALUES(%s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(insertProfesorSQL, (id_persona, asignatura, salario))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updateProfesor(self, id_profesor, asignatura, salario):
        updateProfesorSQL = """
        UPDATE profesor
        SET asignatura=%s, salario=%s
        WHERE id_profesor=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(updateProfesorSQL, (asignatura, salario, id_profesor))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deleteProfesor(self, id_profesor):
        deleteProfesorSQL = """
        DELETE FROM profesor
        WHERE id_profesor=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(deleteProfesorSQL, (id_profesor,))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
