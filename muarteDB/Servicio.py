from db_connection import DBConnection

class ServicioCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_servicio(self,precio_base, descripcion, tipo_danio, estado_mueble,foto_disenio, nombre_disenio, estilo, tipo_mueble, duracion_estimada):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = """
            INSERT INTO Servicio (precio_base, descripcion, tipo_danio, estado_Mueble, foto_disenio, nombreDisenio, estilo, tipoMueble, duracionEstimada)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
          """
        valores = (precio_base, descripcion, tipo_danio, estado_mueble,foto_disenio, nombre_disenio, estilo, tipo_mueble, duracion_estimada)
        cursor.execute(sql, valores)
        conn.commit()
        print("Servicio creado.")
        conn.close()

    def mostrar_servicio(self, id_servicio):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM Servicio WHERE idServicio = %s"
        cursor.execute(sql, (id_servicio,))
        resultado = cursor.fetchone()
        if resultado:
            print("Servicio encontrado:", resultado)
        else:
            print("Servicio no encontrado.")
        conn.close()

    def actualizar_servicio(self, id_servicio, nuevo_costo):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "UPDATE Servicio SET precio_base = %s WHERE idServicio = %s"
        valores = (nuevo_costo, id_servicio)
        cursor.execute(sql, valores)
        conn.commit()
        print("Servicio actualizado.")
        conn.close()

    def eliminar_servicio(self, id_servicio):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM Servicio WHERE idServicio = %s"
        cursor.execute(sql, (id_servicio,))
        conn.commit()
        print("Servicio eliminado.")
        conn.close()
