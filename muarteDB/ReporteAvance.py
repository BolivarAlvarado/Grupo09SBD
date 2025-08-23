from db_connection import DBConnection

class ReporteAvanceCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_reporte(self, foto_avance, detalles_avance, estado_avance, fecha_reporte, id_pedido):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_crear_reporte(%s, %s, %s, %s, %s)"
            valores = (foto_avance, detalles_avance, estado_avance, fecha_reporte, id_pedido)
            cursor.execute(sql, valores)
            conn.commit()
            print("Reporte de avance")
        except Exception as e:
            print("Error al crear reporte:", e)
            conn.rollback()
        finally:
            conn.close()

    def mostrar_reporte(self, id_reporte):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "CALL sp_mostrar_reporte(%s)"
        cursor.execute(sql, (id_reporte,))
        resultado = cursor.fetchone()
        if resultado:
            print("Reporte encontrado:", resultado)
        else:
            print("Reporte no encontrado.")
        conn.close()

    def actualizar_reporte(self, id_reporte, nuevo_estado):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_actualizar_reporte(%s, %s)"
            valores = (id_reporte, nuevo_estado)
            cursor.execute(sql, valores)
            conn.commit()
            print("Reporte de avance actualizado")
        except Exception as e:
            print("Error al actualizar reporte:", e)
            conn.rollback()
        finally:
            conn.close()

    def eliminar_reporte(self, id_reporte):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_eliminar_reporte(%s)"
            cursor.execute(sql, (id_reporte,))
            conn.commit()
            print("Reporte eliminado mediante SP.")
        except Exception as e:
            print("Error al eliminar reporte:", e)
            conn.rollback()
        finally:
            conn.close()

    
    def menu_reporte_avance(self):
        while True:
            print("\n--- CRUD Reporte de Avance ---")
            print("1. Añadir reporte")
            print("2. Consultar reporte")
            print("3. Editar estado de reporte")
            print("4. Eliminar reporte")
            print("0. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    print("\n--- Crear Reporte ---")
                    foto_avance = input("Ruta o descripción de la foto del avance: ")
                    detalles_avance = input("Detalles del avance: ")
                    estado_avance = input("Estado del avance: ")
                    fecha_reporte = input("Fecha del reporte (YYYY-MM-DD): ")
                    try:
                        id_pedido = int(input("ID del pedido: "))
                        self.crear_reporte(foto_avance, detalles_avance, estado_avance, fecha_reporte, id_pedido)
                    except ValueError:
                        print("ID de pedido inválido.")

                case "2":
                    print("\n--- Mostrar Reporte ---")
                    try:
                        id_reporte = int(input("ID del reporte: "))
                        self.mostrar_reporte(id_reporte)
                    except ValueError:
                        print("ID inválido.")

                case "3":
                    print("\n--- Actualizar Estado del Reporte ---")
                    try:
                        id_reporte = int(input("ID del reporte: "))
                        nuevo_estado = input("Nuevo estado del avance: ")
                        self.actualizar_reporte(id_reporte, nuevo_estado)
                    except ValueError:
                        print("ID inválido.")

                case "4":
                    print("\n--- Eliminar Reporte ---")
                    try:
                        id_reporte = int(input("ID del reporte a eliminar: "))
                        confirmacion = input("¿Estás seguro? (s/n): ")
                        if confirmacion.lower() == "s":
                            self.eliminar_reporte(id_reporte)
                        else:
                            print("Eliminación cancelada.")
                    except ValueError:
                        print("ID inválido.")

                case "0":
                    print("Volviendo al menú principal...")
                    break

                case _:
                    print("Opción inválida. Intente de nuevo.")
