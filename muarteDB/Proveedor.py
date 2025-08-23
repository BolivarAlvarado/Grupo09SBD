from db_connection import DBConnection

class ProveedorCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_proveedor(self, nombre, telefono, tipoMaterial, direccion):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_crear_proveedor(%s, %s, %s, %s)"
            valores = (nombre, telefono, tipoMaterial, direccion)
            cursor.execute(sql, valores)
            conn.commit()
            print("Proveedor creado")
        except Exception as e:
            print("Error al crear proveedor:", e)
            conn.rollback()
        finally:
            conn.close()

    def mostrar_proveedor(self, id_proveedor):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "CALL sp_mostrar_proveedor(%s)"
        cursor.execute(sql, (id_proveedor,))
        resultado = cursor.fetchone()
        if resultado:
            print("Proveedor encontrado:", resultado)
        else:
            print("Proveedor no encontrado.")
        conn.close()

    def actualizar_proveedor(self, id_proveedor, nuevo_material):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_actualizar_proveedor(%s, %s)"
            valores = (id_proveedor, nuevo_material)
            cursor.execute(sql, valores)
            conn.commit()
            print("Proveedor actualizado")
        except Exception as e:
            print("Error al actualizar proveedor:", e)
            conn.rollback()
        finally:
            conn.close()

    def eliminar_proveedor(self, id_proveedor):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_eliminar_proveedor(%s)"
            cursor.execute(sql, (id_proveedor,))
            conn.commit()
            print("Proveedor eliminado")
        except Exception as e:
            print("Error al eliminar proveedor:", e)
            conn.rollback()
        finally:
            conn.close()


    def menu_proveedor(self):
        while True:
            print("\n--- CRUD Proveedor ---")
            print("1. Añadir proveedor")
            print("2. Consultar proveedor")
            print("3. Editar proveedor")
            print("4. Eliminar proveedor")
            print("0. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    print("\n--- Crear Proveedor ---")
                    nombre = input("Nombre: ")
                    telefono = input("Teléfono: ")
                    tipo_material = input("Tipo de material: ")
                    direccion = input("Dirección: ")
                    self.crear_Proveedor(nombre, telefono, tipo_material, direccion)

                case "2":
                    print("\n--- Mostrar Proveedor ---")
                    try:
                        id_proveedor = int(input("ID del proveedor: "))
                        self.mostrar_Proveedor(id_proveedor)
                    except ValueError:
                        print("ID inválido.")

                case "3":
                    print("\n--- Actualizar Proveedor ---")
                    try:
                        id_proveedor = int(input("ID del proveedor: "))
                        nuevo_material = input("Nuevo tipo de material: ")
                        self.actualizar_Proveedor(id_proveedor, nuevo_material)
                    except ValueError:
                        print("ID inválido.")

                case "4":
                    print("\n--- Eliminar Proveedor ---")
                    try:
                        id_proveedor = int(input("ID del proveedor a eliminar: "))
                        confirmacion = input("¿Estás seguro? (s/n): ")
                        if confirmacion.lower() == "s":
                            self.eliminar_Proveedor(id_proveedor)
                        else:
                            print("Eliminación cancelada.")
                    except ValueError:
                        print("ID inválido.")

                case "0":
                    print("Volviendo al menú principal...")
                    break

                case _:
                    print("Opción inválida. Intente de nuevo.")