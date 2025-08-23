from db_connection import DBConnection

class ClienteCRUD:

    def __init__(self):
        self.db = DBConnection()

    def crear_cliente(self, direccion, nombre, telefono, correo):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_crear_cliente(%s, %s, %s, %s)"
            valores = (direccion, nombre, telefono, correo)
            cursor.execute(sql, valores)
            conn.commit()
            print("Cliente creado")
        except Exception as e:
            print("Error al crear cliente:", e)
            conn.rollback()
        finally:
            conn.close()


    def mostrar_cliente(self, id_cliente):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "CALL sp_mostrar_cliente(%s)"
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
        try:
            sql = "CALL sp_actualizar_cliente(%s, %s)"
            valores = (id_cliente, nuevo_correo)
            cursor.execute(sql, valores)
            conn.commit()
            print("Cliente actualizado")
        except Exception as e:
            print("Error al actualizar cliente:", e)
            conn.rollback()
        finally:
            conn.close()


    def eliminar_cliente(self, id_cliente):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_eliminar_cliente(%s)"
            cursor.execute(sql, (id_cliente,))
            conn.commit()
            print("Cliente eliminado.")
        except Exception as e:
            print("Error al eliminar cliente:", e)
            conn.rollback()
        finally:
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
