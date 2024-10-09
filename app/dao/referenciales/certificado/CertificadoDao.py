# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class TipoCertificadoDao:

    def getTiposCertificados(self):
        tipo_certificadoSQL = """
        SELECT id, descripcion
        FROM tipo_certificados
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tipo_certificadoSQL)
            # trae datos de la bd
            lista_tipo_certificados = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_tipo_certificados:
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

    def getTipoCertificadoById(self, id):
        tipo_certificadoSQL = """
        SELECT id, descripcion
        FROM tipo_certificados WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tipo_certificadoSQL, (id,))
            # trae datos de la bd
            tipo_certificadoEncontrado = cur.fetchone()
            # retorno los datos
            return {
                "id": tipo_certificadoEncontrado[0],
                "descripcion": tipo_certificadoEncontrado[1]
            }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarTipoCertificado(self, descripcion):
        insertTipoCertificadoSQL = """
        INSERT INTO tipo_certificados(descripcion) VALUES(%s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertTipoCertificadoSQL, (descripcion,))
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

    def updateTipoCertificado(self, id, descripcion):
        updateTipoCertificadoSQL = """
        UPDATE tipo_certificados
        SET descripcion=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateTipoCertificadoSQL, (descripcion, id,))
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

    def deleteTipoCertificado(self, id):
        deleteTipoCertificadoSQL = """
        DELETE FROM tipo_certificados
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(deleteTipoCertificadoSQL, (id,))
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
