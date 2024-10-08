from flask import current_app as app
from app.conexion.Conexion import Conexion

class AsignaturaDao:

    def getAsignaturas(self):
        asignaturaSQL = """
        SELECT id, nombre_estudiante, curso, asignatura
        FROM asignaturas
        """
        # Objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(asignaturaSQL)
            # Trae datos de la base de datos
            lista_asignaturas = cur.fetchall()
            # Retorna los datos
            lista_ordenada = []
            for item in lista_asignaturas:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre_estudiante": item[1],
                    "curso": item[2],
                    "asignatura": item[3]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getAsignaturaById(self, id):
        asignaturaSQL = """
        SELECT id, nombre_estudiante, curso, asignatura
        FROM asignaturas WHERE id=%s
        """
        # Objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(asignaturaSQL, (id,))
            # Trae datos de la base de datos
            asignaturaEncontrada = cur.fetchone()
            # Retorna los datos
            return {
                "id": asignaturaEncontrada[0],
                "nombre_estudiante": asignaturaEncontrada[1],
                "curso": asignaturaEncontrada[2],
                "asignatura": asignaturaEncontrada[3]
            }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarAsignatura(self, nombre_estudiante, curso, asignatura):
        insertAsignaturaSQL = """
        INSERT INTO asignaturas(nombre_estudiante, curso, asignatura) 
        VALUES(%s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecución exitosa
        try:
            cur.execute(insertAsignaturaSQL, (nombre_estudiante, curso, asignatura))
            # Confirma la inserción
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updateAsignatura(self, id, nombre_estudiante, curso, asignatura):
        updateAsignaturaSQL = """
        UPDATE asignaturas
        SET nombre_estudiante=%s, curso=%s, asignatura=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecución exitosa
        try:
            cur.execute(updateAsignaturaSQL, (nombre_estudiante, curso, asignatura, id))
            # Confirma la actualización
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deleteAsignatura(self, id):
        deleteAsignaturaSQL = """
        DELETE FROM asignaturas
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecución exitosa
        try:
            cur.execute(deleteAsignaturaSQL, (id,))
            # Confirma la eliminación
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
