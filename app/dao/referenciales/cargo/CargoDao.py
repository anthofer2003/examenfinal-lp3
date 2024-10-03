# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class CargoDao:

    def getCargos(self):
        # Consulta para obtener todos los cargos
        cargoSQL = """
        SELECT id, nombre, apellido, numero_de_cedula, cargo
        FROM cargos
        """
        # Objeto conexión
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cargoSQL)
            # Trae datos de la base de datos
            lista_cargos = cur.fetchall()
            # Retorno los datos
            lista_ordenada = []
            for item in lista_cargos:
                lista_ordenada.append({
                    "id": item[0],
                    "nombre": item[1],
                    "apellido": item[2],
                    "numero_de_cedula": item[3],
                    "cargo": item[4]
                })
            return lista_ordenada
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def getCargoById(self, id):
        # Consulta para obtener un cargo específico
        cargoSQL = """
        SELECT id, nombre, apellido, numero_de_cedula, cargo
        FROM cargos WHERE id=%s
        """
        # Objeto conexión
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cargoSQL, (id,))
            # Trae datos de la base de datos
            cargoEncontrado = cur.fetchone()
            # Retorno los datos
            return {
                "id": cargoEncontrado[0],
                "nombre": cargoEncontrado[1],
                "apellido": cargoEncontrado[2],
                "numero_de_cedula": cargoEncontrado[3],
                "cargo": cargoEncontrado[4]
            }
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

    def guardarCargo(self, nombre, apellido, numero_de_cedula, cargo):
        # Inserta un nuevo cargo en la base de datos
        insertCargoSQL = """
        INSERT INTO cargos(nombre, apellido, numero_de_cedula, cargo) 
        VALUES(%s, %s, %s, %s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecución exitosa
        try:
            cur.execute(insertCargoSQL, (nombre, apellido, numero_de_cedula, cargo))
            # Se confirma la inserción
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def updateCargo(self, id, nombre, apellido, numero_de_cedula, cargo):
        # Actualiza un cargo existente en la base de datos
        updateCargoSQL = """
        UPDATE cargos
        SET nombre=%s, apellido=%s, numero_de_cedula=%s, cargo=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecución exitosa
        try:
            cur.execute(updateCargoSQL, (nombre, apellido, numero_de_cedula, cargo, id))
            # Se confirma la actualización
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False

    def deleteCargo(self, id):
        # Elimina un cargo de la base de datos
        deleteCargoSQL = """
        DELETE FROM cargos
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecución exitosa
        try:
            cur.execute(deleteCargoSQL, (id,))
            # Se confirma la eliminación
            con.commit()
            return True
        except con.Error as e:
            app.logger.info(e)
        finally:
            cur.close()
            con.close()

        return False
