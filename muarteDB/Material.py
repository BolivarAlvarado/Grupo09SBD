from db_connection import DBConnection
from datetime import datetime

class MaterialCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_material(self, descripcion, stock, color, tipo_material, costo_material, stock_minimo, id_proveedor):
        conn = self.db.conectar()
        cursor = conn.cursor()
        fecha_ingreso = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            sql = "CALL sp_crear_material(%s, %s, %s, %s, %s, %s, %s, %s)"
            valores = (descripcion, stock, color, tipo_material, costo_material, fecha_ingreso, stock_minimo, id_proveedor)
            cursor.execute(sql, valores)
            conn.commit()
            print("Material creado")
        except Exception as e:
            print("Error al crear material:", e)
            conn.rollback()
        finally:
            conn.close()

    def mostrar_material(self, id_material):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "CALL sp_mostrar_material(%s)"
        cursor.execute(sql, (id_material,))
        resultado = cursor.fetchone()
        if resultado:
            print("Material encontrado:", resultado)
        else:
            print("Material no encontrado.")
        conn.close()

    def actualizar_material(self, id_material, nuevo_costo):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_actualizar_material(%s, %s)"
            valores = (id_material, nuevo_costo)
            cursor.execute(sql, valores)
            conn.commit()
            print("Material actualizado")
        except Exception as e:
            print("Error al actualizar material:", e)
            conn.rollback()
        finally:
            conn.close()

    def eliminar_material(self, id_material):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_eliminar_material(%s)"
            cursor.execute(sql, (id_material,))
            conn.commit()
            print("Material eliminado")
        except Exception as e:
            print("Error al eliminar material:", e)
            conn.rollback()
        finally:
            conn.close()


    def menu_material(self):
        while True:
            print("\n--- CRUD Material ---")
            print("1. Añadir material")
            print("2. Consultar materiales")
            print("3. Editar material")
            print("4. Eliminar material")
            print("0. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    print("\n--- Crear Material---")
                    try:
                        descripcion = input("Descripción del material: ")
                        stock = int(input("Cantidad en stock: "))
                        color = input("Color del material: ")
                        tipo = input("Tipo de material: ")
                        costo = float(input("Costo del material: "))
                        stock_min = int(input("Stock mínimo: "))
                        id_proveedor = int(input("ID del proveedor: "))
                        self.crear_material(descripcion, stock, color, tipo, costo, stock_min, id_proveedor)
                    except ValueError:
                        print("Error en los datos ingresados.")

                case "2":
                    print("\n--- Mostrar Material ---")
                    try:
                        id_material = int(input("ID del material: "))
                        self.mostrar_material(id_material)
                    except ValueError:
                        print("ID inválido.")

                case "3":
                    print("\n--- Actualizar Material ---")
                    try:
                        id_material = int(input("ID del material: "))
                        nuevo_costo = float(input("Nuevo costo: "))
                        self.actualizar_material(id_material, nuevo_costo)
                    except ValueError:
                        print("ID inválido.")

                case "4":
                    print("\n--- Eliminar Material ---")
                    try:
                        id_material = int(input("ID del material a eliminar: "))
                        confirmacion = input("¿Estás seguro? (s/n): ")
                        if confirmacion.lower() == "s":
                            self.eliminar_material(id_material)
                        else:
                            print("Eliminación cancelada.")
                    except ValueError:
                        print("ID inválido.")

                case "0":
                    print("Volviendo al menú principal...")
                    break

                case _:
                    print("Opción inválida. Intente de nuevo.")
