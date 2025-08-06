from db_connection import DBConnection

class TransportistaCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_transportista(self, nombre, telefono, disponibilidad, zona_cobertura):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO Transportista (nombre, numTelefono, disponibilidad, zonaCobertura) VALUES (%s, %s, %s, %s)"
        valores = (nombre, telefono, disponibilidad, zona_cobertura)
        cursor.execute(sql, valores)
        conn.commit()
        print("Transportista creado.")
        conn.close()

    def mostrar_transportista(self, id_transportista):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM Transportista WHERE idTransportista = %s"
        cursor.execute(sql, (id_transportista,))
        resultado = cursor.fetchone()
        if resultado:
            print("Transportista encontrado:", resultado)
        else:
            print("Transportista no encontrado.")
        conn.close()

    def actualizar_transportista(self, id_transportista, nueva_disponibilidad):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "UPDATE Transportista SET disponibilidad = %s WHERE idTransportista = %s"
        valores = (nueva_disponibilidad, id_transportista)
        cursor.execute(sql, valores)
        conn.commit()
        print("Transportista actualizado.")
        conn.close()

    def eliminar_transportista(self, id_transportista):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM Transportista WHERE idTransportista = %s"
        cursor.execute(sql, (id_transportista,))
        conn.commit()
        print("Transportista eliminado.")
        conn.close()
