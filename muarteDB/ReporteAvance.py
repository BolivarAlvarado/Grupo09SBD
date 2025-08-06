from db_connection import DBConnection

class ReporteAvanceCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_reporte(self,foto_avance, detalles_avance, estado_avance, fecha_reporte, id_pedido):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO ReporteAvance (fotoAvance, detallesAvance, estadoAvance, estadoAvance, fechaReporte, idPedido) VALUES (%s, %s, %s, %s, %s)"
        valores = (foto_avance, detalles_avance, estado_avance, fecha_reporte, id_pedido)
        cursor.execute(sql, valores)
        conn.commit()
        print("Reporte de avance creado.")
        conn.close()

    def mostrar_reporte(self, id_reporte):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM ReporteAvance WHERE idReporteAvance = %s"
        cursor.execute(sql, (id_reporte,))
        resultado = cursor.fetchone()
        if resultado:
            print("Reporte encontrado:", resultado)
        else:
            print("Reporte no encontrado.")
        conn.close()

    def actualizar_reporte(self, id_reporte, nuevo_estado):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "UPDATE ReporteAvance SET estadoAvance = %s WHERE idReporteAvance = %s"
        valores = (nuevo_estado, id_reporte)
        cursor.execute(sql, valores)
        conn.commit()
        print("Reporte de avance actualizado.")
        conn.close()

    def eliminar_reporte(self, id_reporte):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM ReporteAvance WHERE idReporteAvance = %s"
        cursor.execute(sql, (id_reporte,))
        conn.commit()
        print("Reporte de avance eliminado.")
        conn.close()
