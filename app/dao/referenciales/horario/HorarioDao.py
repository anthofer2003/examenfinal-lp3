# Data access object - DAO para la tabla horarios
from flask import current_app as app
from app.conexion.Conexion import Conexion

class HorarioDao:

    def getHorarios(self):
        horarioSQL = """
        SELECT id, curso, nombre_profesor, dia, hora_inicio, hora_fin, aula
        FROM horarios
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(horarioSQL)
            # trae datos de la bd
            lista_horarios = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_horarios:
                lista_ordenada.append({
                    "id": item[0],
                    "curso": item[1],
                    "nombre_profesor": item[2],
                    "dia": item[3],
                    "hora_inicio": item[4].strftime("%H:%M:%S"),
                    "hora_fin": item[5].strftime("%H:%M:%S"),
                    "aula": item[6]
                })
            return lista_ordenada
        except Exception as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getHorarioById(self, id):
        horarioSQL = """
        SELECT id, curso, nombre_profesor, dia, hora_inicio, hora_fin, aula
        FROM horarios WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(horarioSQL, (id,))
            # trae datos de la bd
            horarioEncontrado = cur.fetchone()
            if horarioEncontrado:
                return {
                    "id": horarioEncontrado[0],
                    "curso": horarioEncontrado[1],
                    "nombre_profesor": horarioEncontrado[2],
                    "dia": horarioEncontrado[3],
                    "hora_inicio": horarioEncontrado[4].strftime("%H:%M:%S"),
                    "hora_fin": horarioEncontrado[5].strftime("%H:%M:%S"),
                    "aula": horarioEncontrado[6]
                }
            else:
                return None
        except Exception as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarHorario(self, curso, nombre_profesor, dia, hora_inicio, hora_fin, aula):
        insertHorarioSQL = """
        INSERT INTO horarios(curso, nombre_profesor, dia, hora_inicio, hora_fin, aula) 
        VALUES(%s, %s, %s, %s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(insertHorarioSQL, (curso, nombre_profesor, dia, hora_inicio, hora_fin, aula))
            con.commit()
            return True
        except Exception as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updateHorario(self, id, curso, nombre_profesor, dia, hora_inicio, hora_fin, aula):
        updateHorarioSQL = """
        UPDATE horarios
        SET curso=%s, nombre_profesor=%s, dia=%s, hora_inicio=%s, hora_fin=%s, aula=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateHorarioSQL, (curso, nombre_profesor, dia, hora_inicio, hora_fin, aula, id))
            con.commit()
            return True
        except Exception as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deleteHorario(self, id):
        deleteHorarioSQL = """
        DELETE FROM horarios
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteHorarioSQL, (id,))
            con.commit()
            return True
        except Exception as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
