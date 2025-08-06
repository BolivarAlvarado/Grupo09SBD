from db_connection import DBConnection

class PagoCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_pago(self, metodo_pago, fecha_pago, descuento, subtotal, iva, monto_pago, id_pedido):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO Pago (metodoPago, fechaPago, descuento, subtotal, iva, montoPago, idPedido) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (metodo_pago, fecha_pago, descuento, subtotal, iva, monto_pago, id_pedido)
        cursor.execute(sql, valores)
        conn.commit()
        print("Pago registrado.")
        conn.close()

    def mostrar_pago(self, id_pago):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM Pago WHERE idPago = %s"
        cursor.execute(sql, (id_pago,))
        resultado = cursor.fetchone()
        if resultado:
            print("Pago encontrado:", resultado)
        else:
            print("Pago no encontrado.")
        conn.close()

    def actualizar_pago(self, id_pago, nuevo_total):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "UPDATE Pago SET montoPago = %s WHERE idPago = %s"
        valores = (nuevo_total, id_pago)
        cursor.execute(sql, valores)
        conn.commit()
        print("Pago actualizado.")
        conn.close()

    def eliminar_pago(self, id_pago):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM Pago WHERE idPago = %s"
        cursor.execute(sql, (id_pago,))
        conn.commit()
        print("Pago eliminado.")
        conn.close()
