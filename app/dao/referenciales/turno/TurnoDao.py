from flask import current_app as app
from app.conexion.Conexion import Conexion

class TurnoDao:

    def getTurnos(self):
        turnoSQL = """
        SELECT id, descripcion
        FROM turnos
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(turnoSQL)
            # trae datos de la bd
            lista_turnos = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_turnos:
                lista_ordenada.append({
                    "id": item[0],
                    "descripcion": item[1]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getTurnoById(self, id):
        turnoSQL = """
        SELECT id, descripcion
        FROM turnos WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(turnoSQL, (id,))
            # trae datos de la bd
            turnoEncontrado = cur.fetchone()
            # retorno los datos
            return {
                "id": turnoEncontrado[0],
                "descripcion": turnoEncontrado[1]
            } if turnoEncontrado else None
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarTurno(self, descripcion):
        insertTurnoSQL = """
        INSERT INTO turnos(descripcion) VALUES(%s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertTurnoSQL, (descripcion,))
            # se confirma la insercion
            con.commit()
            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def updateTurno(self, id, descripcion):
        updateTurnoSQL = """
        UPDATE turnos
        SET descripcion=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateTurnoSQL, (descripcion, id,))
            # se confirma la insercion
            con.commit()
            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False

    def deleteTurno(self, id):
        deleteTurnoSQL = """
        DELETE FROM turnos
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteTurnoSQL, (id,))
            # se confirma la insercion
            con.commit()
            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False
