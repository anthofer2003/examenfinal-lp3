# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ProfesorDao:

    def getProfesores(self):
        profesoresSQL = """
        SELECT id_profesor, nombre_profesor, apellido_profesor, titulo_academico, correo, telefono
        FROM profesores
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(profesoresSQL)
            # trae datos de la bd
            lista_profesores = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_profesores:
                lista_ordenada.append({
                    "id_profesor": item[0],
                    "nombre_profesor": item[1],
                    "apellido_profesor": item[2],
                    "titulo_academico": item[3],
                    "correo": item[4],
                    "telefono": item[5]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getProfesorById(self, id_profesor):
        profesorSQL = """
        SELECT id_profesor, nombre_profesor, apellido_profesor, titulo_academico, correo, telefono
        FROM profesores WHERE id_profesor=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(profesorSQL, (id_profesor,))
            # trae datos de la bd
            profesorEncontrado = cur.fetchone()
            # retorno los datos
            if profesorEncontrado:
                return {
                    "id_profesor": profesorEncontrado[0],
                    "nombre_profesor": profesorEncontrado[1],
                    "apellido_profesor": profesorEncontrado[2],
                    "titulo_academico": profesorEncontrado[3],
                    "correo": profesorEncontrado[4],
                    "telefono": profesorEncontrado[5]
                }
            return None
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarProfesor(self, nombre_profesor, apellido_profesor, titulo_academico, correo, telefono):
        insertProfesorSQL = """
        INSERT INTO profesores(nombre_profesor, apellido_profesor, titulo_academico, correo, telefono) 
        VALUES(%s, %s, %s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertProfesorSQL, (nombre_profesor, apellido_profesor, titulo_academico, correo, telefono))
            # se confirma la insercion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updateProfesor(self, id_profesor, nombre_profesor, apellido_profesor, titulo_academico, correo, telefono):
        updateProfesorSQL = """
        UPDATE profesores
        SET nombre_profesor=%s, apellido_profesor=%s, titulo_academico=%s, correo=%s, telefono=%s
        WHERE id_profesor=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateProfesorSQL, (nombre_profesor, apellido_profesor, titulo_academico, correo, telefono, id_profesor))
            # se confirma la insercion
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
        DELETE FROM profesores
        WHERE id_profesor=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteProfesorSQL, (id_profesor,))
            # se confirma la insercion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
