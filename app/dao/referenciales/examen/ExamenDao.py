# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class TipoExamenDao:

    def getTiposExamenes(self):
        tipo_examen_sql = """
        SELECT id, descripcion
        FROM tipo_examenes
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tipo_examen_sql)
            # trae datos de la bd
            lista_tipos_examenes = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_tipos_examenes:
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

    def getTipoExamenById(self, id):
        tipo_examen_sql = """
        SELECT id, descripcion
        FROM tipo_examenes WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tipo_examen_sql, (id,))
            # trae datos de la bd
            tipo_examen_encontrado = cur.fetchone()
            # retorno los datos
            return {
                "id": tipo_examen_encontrado[0],
                "descripcion": tipo_examen_encontrado[1]
            }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarTipoExamen(self, descripcion):
        insert_tipo_examen_sql = """
        INSERT INTO tipo_examenes(descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insert_tipo_examen_sql, (descripcion,))
            # se confirma la insercion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updateTipoExamen(self, id, descripcion):
        update_tipo_examen_sql = """
        UPDATE tipo_examenes
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(update_tipo_examen_sql, (descripcion, id,))
            # se confirma la insercion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deleteTipoExamen(self, id):
        delete_tipo_examen_sql = """
        DELETE FROM tipo_examenes
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(delete_tipo_examen_sql, (id,))
            # se confirma la eliminacion
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
