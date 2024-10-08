# Data access object - DAO para la tabla cursos_particulares
from flask import current_app as app
from app.conexion.Conexion import Conexion

class CursoParticularDao:

    def getCursosParticulares(self):
        cursoSQL = """
        SELECT id, curso, fecha_inicio, fecha_fin, precio_mes
        FROM cursos_particulares
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cursoSQL)
            # trae datos de la bd
            lista_cursos = cur.fetchall()
            # retorno los datos
            lista_ordenada = []
            for item in lista_cursos:
                lista_ordenada.append({
                    "id": item[0],
                    "curso": item[1],
                    "fecha_inicio": item[2].strftime("%Y-%m-%d"),
                    "fecha_fin": item[3].strftime("%Y-%m-%d"),
                    "precio_mes": item[4]
                })
            return lista_ordenada
        except Exception as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getCursoParticularById(self, id):
        cursoSQL = """
        SELECT id, curso, fecha_inicio, fecha_fin, precio_mes
        FROM cursos_particulares WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cursoSQL, (id,))
            # trae datos de la bd
            cursoEncontrado = cur.fetchone()
            if cursoEncontrado:
                return {
                    "id": cursoEncontrado[0],
                    "curso": cursoEncontrado[1],
                    "fecha_inicio": cursoEncontrado[2].strftime("%Y-%m-%d"),
                    "fecha_fin": cursoEncontrado[3].strftime("%Y-%m-%d"),
                    "precio_mes": cursoEncontrado[4]
                }
            else:
                return None
        except Exception as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarCursoParticular(self, curso, fecha_inicio, fecha_fin, precio_mes):
        insertCursoSQL = """
        INSERT INTO cursos_particulares(curso, fecha_inicio, fecha_fin, precio_mes) 
        VALUES(%s, %s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(insertCursoSQL, (curso, fecha_inicio, fecha_fin, precio_mes))
            con.commit()
            return True
        except Exception as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updateCursoParticular(self, id, curso, fecha_inicio, fecha_fin, precio_mes):
        updateCursoSQL = """
        UPDATE cursos_particulares
        SET curso=%s, fecha_inicio=%s, fecha_fin=%s, precio_mes=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateCursoSQL, (curso, fecha_inicio, fecha_fin, precio_mes, id))
            con.commit()
            return True
        except Exception as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deleteCursoParticular(self, id):
        deleteCursoSQL = """
        DELETE FROM cursos_particulares
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteCursoSQL, (id,))
            con.commit()
            return True
        except Exception as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
