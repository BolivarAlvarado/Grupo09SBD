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

    def menu_cliente(self):
        while True:
            print("\n--- CRUD Cliente ---")
            print("1. Añadir cliente")
            print("2. Consultar clientes")
            print("3. Editar cliente")
            print("4. Eliminar cliente")
            print("0. Volver al menú principal")
    
            opcion = input("Seleccione una opción: ")
    
            match opcion:
                case "1":
                    print("\n--- Crear Cliente ---")
                    direccion = input("Dirección: ")
                    nombre = input("Nombre: ")
                    telefono = input("Teléfono: ")
                    correo = input("Correo: ")
                    self.crear_cliente(direccion, nombre, telefono, correo)
    
                case "2":
                    print("\n--- Mostrar Cliente ---")
                    try:
                        id_cliente = int(input("ID del cliente: "))
                        self.mostrar_cliente(id_cliente)
                    except ValueError:
                        print("ID inválido.")
    
                case "3":
                    print("\n--- Actualizar Cliente ---")
                    try:
                        id_cliente = int(input("ID del cliente: "))
                        nuevo_correo = input("Nuevo correo: ")
                        self.actualizar_cliente(id_cliente, nuevo_correo)
                    except ValueError:
                        print("ID inválido.")
    
                case "4":
                    print("\n--- Eliminar Cliente ---")
                    try:
                        id_cliente = int(input("ID del cliente a eliminar: "))
                        confirmacion = input("¿Estás seguro? (s/n): ")
                        if confirmacion.lower() == "s":
                            self.eliminar_cliente(id_cliente)
                        else:
                            print("Eliminación cancelada.")
                    except ValueError:
                        print("ID inválido.")
    
                case "0":
                    print("Volviendo al menú principal...")
                    break
    
                case _:
                    print("Opción inválida. Intente de nuevo.")
