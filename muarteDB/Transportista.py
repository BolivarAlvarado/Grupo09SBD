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
        
    def menu_transportista(self):
        while True:
            print("\n--- CRUD Transportista ---")
            print("1. Añadir transportista")
            print("2. Consultar transportista")
            print("3. Editar disponibilidad")
            print("4. Eliminar transportista")
            print("0. Volver al menú principal")
    
            opcion = input("Seleccione una opción: ")
    
            match opcion:
                case "1":
                    print("\n--- Crear Transportista ---")
                    nombre = input("Nombre: ")
                    telefono = input("Teléfono: ")
                    disponibilidad = input("Disponibilidad (Sí/No): ")
                    zona_cobertura = input("Zona de cobertura: ")
                    transportista_crud.crear_transportista(nombre, telefono, disponibilidad, zona_cobertura)
    
                case "2":
                    print("\n--- Mostrar Transportista ---")
                    try:
                        id_transportista = int(input("ID del transportista: "))
                        transportista_crud.mostrar_transportista(id_transportista)
                    except ValueError:
                        print("ID inválido.")
    
                case "3":
                    print("\n--- Actualizar Disponibilidad ---")
                    try:
                        id_transportista = int(input("ID del transportista: "))
                        nueva_disponibilidad = input("Nueva disponibilidad (Sí/No): ")
                        transportista_crud.actualizar_transportista(id_transportista, nueva_disponibilidad)
                    except ValueError:
                        print("ID inválido.")
    
                case "4":
                    print("\n--- Eliminar Transportista ---")
                    try:
                        id_transportista = int(input("ID del transportista a eliminar: "))
                        confirmacion = input("¿Estás seguro? (s/n): ")
                        if confirmacion.lower() == "s":
                            transportista_crud.eliminar_transportista(id_transportista)
                        else:
                            print("Eliminación cancelada.")
                    except ValueError:
                        print("ID inválido.")
    
                case "0":
                    print("Volviendo al menú principal...")
                    break
    
                case _:
                    print("Opción inválida. Intente de nuevo.")
