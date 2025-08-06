from db_connection import DBConnection

class ProveedorCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_Proveedor(self, nombre, telefono, tipoMaterial, direccion):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO Proveedor(nombre, num_telefono, tipo_material, direccion) VALUES (%s, %s, %s, %s)"
        valores = (nombre, telefono, tipoMaterial, direccion)
        cursor.execute(sql,valores)
        conn.commit()
        print("Proveedor Creado")
        conn.close()

    def mostrar_Proveedor(self, id_proveedor):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM Proveedor WHERE idProveedor = %s"
        cursor.execute(sql, (id_proveedor,))
        resultado = cursor.fetchone()
        if resultado:
            print("Proveedor encontrado:", resultado)
        else:
            print("Proveedor no encontrado.")
        conn.close()

    def actualizar_Proveedor(self, id_proveedor, nuevo_material):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "UPDATE Proveedor SET tipo_material = %s WHERE idProveedor = %s"
        valores = (nuevo_material, id_proveedor)
        cursor.execute(sql, valores)
        conn.commit()
        print("Proveedor actualizado.")
        conn.close()

    def eliminar_Proveedor(self, id_proveedor):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM Proveedor WHERE idProveedor = %s"
        cursor.execute(sql, (id_proveedor,))
        conn.commit()
        print("Proveedor eliminado.")
        conn.close()

