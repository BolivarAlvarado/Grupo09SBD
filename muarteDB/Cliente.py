from db_connection import DBConnection

class ClienteCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_cliente(self, direccion, nombre, telefono, correo):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO Cliente (direccion, nombre, numTelefono, correo) VALUES (%s, %s, %s, %s)"
        valores = (direccion, nombre, telefono, correo)
        cursor.execute(sql, valores)
        conn.commit()
        print("Cliente creado.")
        conn.close()

    def mostrar_cliente(self, id_cliente):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM Cliente WHERE idCliente = %s"
        cursor.execute(sql, (id_cliente,))
        resultado = cursor.fetchone()
        if resultado:
            print("Cliente encontrado:", resultado)
        else:
            print("Cliente no encontrado.")
        conn.close()

    def actualizar_cliente(self, id_cliente, nuevo_correo):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "UPDATE Cliente SET correo = %s WHERE idCliente = %s"
        valores = (nuevo_correo, id_cliente)
        cursor.execute(sql, valores)
        conn.commit()
        print("Cliente actualizado.")
        conn.close()

    def eliminar_cliente(self, id_cliente):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM Cliente WHERE idCliente = %s"
        cursor.execute(sql, (id_cliente,))
        conn.commit()
        print("Cliente eliminado.")
        conn.close()