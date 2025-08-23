from db_connection import DBConnection

class TransportistaCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_transportista(self, nombre, telefono, disponibilidad, zona_cobertura):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_crear_transportista(%s, %s, %s, %s)"
            cursor.execute(sql, (nombre, telefono, disponibilidad, zona_cobertura))
            conn.commit()
            print("Transportista creado")
        except Exception as e:
            print("Error al crear transportista:", e)
            conn.rollback()
        finally:
            conn.close()

    def mostrar_transportista(self, id_transportista):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "CALL sp_mostrar_transportista(%s)"
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
        try:
            sql = "CALL sp_actualizar_transportista(%s, %s)"
            cursor.execute(sql, (id_transportista, nueva_disponibilidad))
            conn.commit()
            print("Transportista actualizado")
        except Exception as e:
            print("Error al actualizar transportista:", e)
            conn.rollback()
        finally:
            conn.close()

    def eliminar_transportista(self, id_transportista):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_eliminar_transportista(%s)"
            cursor.execute(sql, (id_transportista,))
            conn.commit()
            print("Transportista eliminado")
        except Exception as e:
            print("Error al eliminar transportista:", e)
            conn.rollback()
        finally:
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
                    self.crear_transportista(nombre, telefono, disponibilidad, zona_cobertura)

                case "2":
                    print("\n--- Mostrar Transportista ---")
                    try:
                        id_transportista = int(input("ID del transportista: "))
                        self.mostrar_transportista(id_transportista)
                    except ValueError:
                        print("ID inválido.")

                case "3":
                    print("\n--- Actualizar Disponibilidad ---")
                    try:
                        id_transportista = int(input("ID del transportista: "))
                        nueva_disponibilidad = input("Nueva disponibilidad (Sí/No): ")
                        self.actualizar_transportista(id_transportista, nueva_disponibilidad)
                    except ValueError:
                        print("ID inválido.")

                case "4":
                    print("\n--- Eliminar Transportista ---")
                    try:
                        id_transportista = int(input("ID del transportista a eliminar: "))
                        confirmacion = input("¿Estás seguro? (s/n): ")
                        if confirmacion.lower() == "s":
                            self.eliminar_transportista(id_transportista)
                        else:
                            print("Eliminación cancelada.")
                    except ValueError:
                        print("ID inválido.")

                case "0":
                    print("Volviendo al menú principal...")
                    break

                case _:
                    print("Opción inválida. Intente de nuevo.")

