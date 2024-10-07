# Data access object - DAO para programas
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ProgramaDao:

    def getProgramas(self):
        programaSQL = """
        SELECT id, nombre, facultad, duracion
        FROM programas
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(programaSQL)
            # trae datos de la bd
            lista_programas = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_programas:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "facultad": item[2],
                    "duracion": item[3]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getProgramaById(self, id):
        programaSQL = """
        SELECT id, nombre, facultad, duracion
        FROM programas WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(programaSQL, (id,))
            # trae datos de la bd
            programaEncontrado = cur.fetchone()
            # retorno los datos
            if programaEncontrado:
                return {
                    "id": programaEncontrado[0],
                    "nombre": programaEncontrado[1],
                    "facultad": programaEncontrado[2],
                    "duracion": programaEncontrado[3]
                }
            return None  # Si no se encuentra el programa
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarPrograma(self, nombre, facultad, duracion):
        insertProgramaSQL = """
        INSERT INTO programas(nombre, facultad, duracion) VALUES(%s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertProgramaSQL, (nombre, facultad, duracion))
            # se confirma la inserción
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updatePrograma(self, id, nombre, facultad, duracion):
        updateProgramaSQL = """
        UPDATE programas
        SET nombre=%s, facultad=%s, duracion=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateProgramaSQL, (nombre, facultad, duracion, id))
            # se confirma la actualización
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deletePrograma(self, id):
        deleteProgramaSQL = """
        DELETE FROM programas
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteProgramaSQL, (id,))
            # se confirma la eliminación
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
