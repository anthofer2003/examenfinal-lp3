# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class PacienteDao:

    def getPacientes(self):
        pacienteSQL = """
        SELECT id, nombre, apellido, fecha_nacimiento, correo, direccion, genero
        FROM pacientes
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(pacienteSQL)
            # trae datos de la bd
            lista_pacientes = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_pacientes:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "apellido": item[2],
                    "fecha_nacimiento": item[3],
                    "correo": item[4],
                    "direccion": item[5],
                    "genero": item[6]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(f"Error al obtener pacientes: {e}")
            return []
        finally:
            cur.close()
            con.close()

    def getPacienteById(self, id_paciente):
        pacienteSQL = """
        SELECT id, nombre, apellido, fecha_nacimiento, correo, direccion, genero
        FROM pacientes WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(pacienteSQL, (id_paciente,))
            # trae datos de la bd
            pacienteEncontrado = cur.fetchone()
            # retorno los datos
            if pacienteEncontrado:
                return {
                    "id": pacienteEncontrado[0],
                    "nombre": pacienteEncontrado[1],
                    "apellido": pacienteEncontrado[2],
                    "fecha_nacimiento": pacienteEncontrado[3],
                    "correo": pacienteEncontrado[4],
                    "direccion": pacienteEncontrado[5],
                    "genero": pacienteEncontrado[6]
                }
            return None
        except con.Error as e:
            app.logger.info(f"Error al obtener paciente por ID: {e}")
            return None
        finally:
            cur.close()
            con.close()

    def guardarPaciente(self, nombre, apellido, fecha_nacimiento, correo, direccion, genero):
        insertPacienteSQL = """
        INSERT INTO pacientes(nombre, apellido, fecha_nacimiento, correo, direccion, genero)
        VALUES(%s, %s, %s, %s, %s, %s)
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertPacienteSQL, (nombre, apellido, fecha_nacimiento, correo, direccion, genero))
            # se confirma la insercion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(f"Error al guardar paciente: {e}")
            return False
        finally:
            cur.close()
            con.close()

    def updatePaciente(self, id_paciente, nombre, apellido, fecha_nacimiento, correo, direccion, genero):
        updatePacienteSQL = """
        UPDATE pacientes
        SET nombre=%s, apellido=%s, fecha_nacimiento=%s, correo=%s, direccion=%s, genero=%s
        WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updatePacienteSQL, (nombre, apellido, fecha_nacimiento, correo, direccion, genero, id_paciente))
            # se confirma la actualizacion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(f"Error al actualizar paciente: {e}")
            return False
        finally:
            cur.close()
            con.close()

    def deletePaciente(self, id_paciente):
        deletePacienteSQL = """
        DELETE FROM pacientes WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deletePacienteSQL, (id_paciente,))
            # se confirma la eliminación
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(f"Error al eliminar paciente: {e}")
            return False
        finally:
            cur.close()
            con.close()
