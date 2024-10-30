# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class PersonaDao:

    def getPersonas(self):
        personasSQL = """
        SELECT id, nombre, apellido, numero_de_cedula, fecha_nac, sexo
        FROM personas
        """
        # Objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personasSQL)
            lista_personas = cur.fetchall()
            lista_ordenada = []
            for item in lista_personas:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "apellido": item[2],
                    "numero_de_cedula": item[3],
                    "fecha_nac": item[4],
                    "sexo": item[5]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getPersonaById(self, id):
        personaSQL = """
        SELECT id, nombre, apellido, numero_de_cedula, fecha_nac, sexo
        FROM personas WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personaSQL, (id,))
            personaEncontrada = cur.fetchone()
            return {
                "id": personaEncontrada[0],
                "nombre": personaEncontrada[1],
                "apellido": personaEncontrada[2],
                "numero_de_cedula": personaEncontrada[3],
                "fecha_nac": personaEncontrada[4],
                "sexo": personaEncontrada[5]
            }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarPersona(self, nombre, apellido, numero_de_cedula, fecha_nac, sexo):
        insertPersonaSQL = """
        INSERT INTO personas(nombre, apellido, numero_de_cedula, fecha_nac, sexo) 
        VALUES(%s, %s, %s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(insertPersonaSQL, (nombre, apellido, numero_de_cedula, fecha_nac, sexo))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updatePersona(self, id, nombre, apellido, numero_de_cedula, fecha_nac, sexo):
        updatePersonaSQL = """
        UPDATE personas
        SET nombre=%s, apellido=%s, numero_de_cedula=%s, fecha_nac=%s, sexo=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(updatePersonaSQL, (nombre, apellido, numero_de_cedula, fecha_nac, sexo, id))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deletePersona(self, id):
        deletePersonaSQL = """
        DELETE FROM personas
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(deletePersonaSQL, (id,))
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
