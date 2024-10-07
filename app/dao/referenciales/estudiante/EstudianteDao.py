# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class EstudianteDao:

    def getEstudiantes(self):
        estudianteSQL = """
        SELECT id, nombre, apellido, fecha_nacimiento, telefono, direccion
        FROM estudiantes
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(estudianteSQL)
            # trae datos de la bd
            lista_estudiantes = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_estudiantes:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "apellido": item[2],
                    "fecha_nacimiento": item[3],
                    "telefono": item[4],
                    "direccion": item[5]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(f"Error al obtener estudiantes: {e}")
            return []
        finally:
            cur.close()
            con.close()

    def getEstudianteById(self, id_estudiante):
        estudianteSQL = """
        SELECT id, nombre, apellido, fecha_nacimiento, telefono, direccion
        FROM estudiantes WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(estudianteSQL, (id_estudiante,))
            # trae datos de la bd
            estudianteEncontrado = cur.fetchone()
            # retorno los datos
            if estudianteEncontrado:
                return {
                    "id": estudianteEncontrado[0],
                    "nombre": estudianteEncontrado[1],
                    "apellido": estudianteEncontrado[2],
                    "fecha_nacimiento": estudianteEncontrado[3],
                    "telefono": estudianteEncontrado[4],
                    "direccion": estudianteEncontrado[5]
                }
            return None
        except con.Error as e:
            app.logger.info(f"Error al obtener estudiante por ID: {e}")
            return None
        finally:
            cur.close()
            con.close()

    def guardarEstudiante(self, nombre, apellido, fecha_nacimiento, telefono, direccion):
        insertEstudianteSQL = """
        INSERT INTO estudiantes(nombre, apellido, fecha_nacimiento, telefono, direccion)
        VALUES(%s, %s, %s, %s, %s)
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertEstudianteSQL, (nombre, apellido, fecha_nacimiento, telefono, direccion))
            # se confirma la insercion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(f"Error al guardar estudiante: {e}")
            return False
        finally:
            cur.close()
            con.close()

    def updateEstudiante(self, id_estudiante, nombre, apellido, fecha_nacimiento, telefono, direccion):
        updateEstudianteSQL = """
        UPDATE estudiantes
        SET nombre=%s, apellido=%s, fecha_nacimiento=%s, telefono=%s, direccion=%s
        WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateEstudianteSQL, (nombre, apellido, fecha_nacimiento, telefono, direccion, id_estudiante))
            # se confirma la actualizacion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(f"Error al actualizar estudiante: {e}")
            return False
        finally:
            cur.close()
            con.close()

    def deleteEstudiante(self, id_estudiante):
        deleteEstudianteSQL = """
        DELETE FROM estudiantes WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteEstudianteSQL, (id_estudiante,))
            # se confirma la eliminación
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(f"Error al eliminar estudiante: {e}")
            return False
        finally:
            cur.close()
            con.close()
