from flask import current_app as app
from app.conexion.Conexion import Conexion
from datetime import datetime  # Importa el módulo datetime

class PersonaDao:

    def getPersonas(self):
        personaSQL = """
        SELECT id_persona, nombres, apellidos, ci, fechanac, 
               creacion_fecha, creacion_hora, creacion_usuario
        FROM personas
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personaSQL)
            lista_personas = cur.fetchall()
            lista_ordenada = []
            for item in lista_personas:
                lista_ordenada.append({
                    "id_persona": item[0],
                    "nombres": item[1],
                    "apellidos": item[2],
                    "ci": item[3],
                    "fechanac": item[4],
                    "creacion_fecha": item[5].strftime("%m/%d/%Y, %H:%M:%S"),
                    "creacion_hora": item[6].strftime("%m/%d/%Y, %H:%M:%S"),
                    "creacion_usuario": item[7]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getPersonaById(self, id_persona):
        personaSQL = """
        SELECT id_persona, nombres, apellidos, ci, fechanac, 
               creacion_fecha, creacion_hora, creacion_usuario
        FROM personas WHERE id_persona=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personaSQL, (id_persona,))
            personaEncontrada = cur.fetchone()
            if personaEncontrada:
                return {
                    "id_persona": personaEncontrada[0],
                    "nombres": personaEncontrada[1],
                    "apellidos": personaEncontrada[2],
                    "ci": personaEncontrada[3],
                    "fechanac": personaEncontrada[4],
                    "creacion_fecha": personaEncontrada[5].strftime("%m/%d/%Y, %H:%M:%S"),
                    "creacion_hora": personaEncontrada[6].strftime("%m/%d/%Y, %H:%M:%S"),
                    "creacion_usuario": personaEncontrada[7]
                }
            return None
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarPersona(self, nombres, apellidos, ci, fechanac, creacion_usuario):
        insertPersonaSQL = """
        INSERT INTO personas(nombres, apellidos, ci, fechanac, 
                             creacion_fecha, creacion_hora, 
                             creacion_usuario) 
        VALUES(%s, %s, %s, %s, %s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            # Obtiene la fecha y hora actuales
            creacion_fecha = datetime.now().date()
            creacion_hora = datetime.now().time()
            
            cur.execute(insertPersonaSQL, (nombres, apellidos, ci, fechanac, creacion_fecha, creacion_hora, creacion_usuario))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updatePersona(self, id_persona, nombres, apellidos, ci, fechanac):
        updatePersonaSQL = """
        UPDATE personas
        SET nombres=%s, apellidos=%s, ci=%s, fechanac=%s
        WHERE id_persona=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(updatePersonaSQL, (nombres, apellidos, ci, fechanac, id_persona))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deletePersona(self, id_persona):
        deletePersonaSQL = """
        DELETE FROM personas
        WHERE id_persona=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(deletePersonaSQL, (id_persona,))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
