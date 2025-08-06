from db_connection import DBConnection

class PedidoCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_pedido(self, fotoEntrega, fechaEntrega, fechaInicio, estado_pedido, id_cliente, id_transportista):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO Pedido (fotoEntrega, fechaEntrega, fechaInicio, estadoPedido, idCliente, idTransportista) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (fotoEntrega, fechaEntrega, fechaInicio, estado_pedido, id_cliente, id_transportista)
        cursor.execute(sql, valores)
        conn.commit()
        print("Pedido creado.")
        conn.close()

    def mostrar_pedido(self, id_pedido):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM Pedido WHERE idPedido = %s"
        cursor.execute(sql, (id_pedido,))
        resultado = cursor.fetchone()
        if resultado:
            print("Pedido encontrado:", resultado)
        else:
            print("Pedido no encontrado.")
        conn.close()

    def actualizar_pedido(self, id_pedido, nuevo_estado):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "UPDATE Pedido SET estadoPedido = %s WHERE idPedido = %s"
        valores = (nuevo_estado, id_pedido)
        cursor.execute(sql, valores)
        conn.commit()
        print("Pedido actualizado.")
        conn.close()

    def eliminar_pedido(self, id_pedido):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM Pedido WHERE idPedido = %s"
        cursor.execute(sql, (id_pedido,))
        conn.commit()
        print("Pedido eliminado.")
        conn.close()
