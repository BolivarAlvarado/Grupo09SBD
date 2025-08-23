from db_connection import DBConnection
import datetime

class EmpleadoCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_empleado(self, nombre, fecha_ingreso, salario_mensual, num_telefono, id_servicio):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_crear_empleado(%s, %s, %s, %s, %s)"
            valores = (nombre, fecha_ingreso, salario_mensual, num_telefono, id_servicio)
            cursor.execute(sql, valores)
            conn.commit()
            print("Empleado creado")
        except Exception as e:
            print("Error al crear empleado:", e)
            conn.rollback()
        finally:
            conn.close()

    def mostrar_empleado(self, id_empleado):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "CALL sp_mostrar_empleado(%s)"
        cursor.execute(sql, (id_empleado,))
        resultado = cursor.fetchone()
        if resultado:
            print("Empleado encontrado:", resultado)
        else:
            print("Empleado no encontrado.")
        conn.close()

    def actualizar_empleado(self, id_empleado, nuevo_servicio):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_actualizar_empleado(%s, %s)"
            valores = (id_empleado, nuevo_servicio)
            cursor.execute(sql, valores)
            conn.commit()
            print("Empleado actualizado")
        except Exception as e:
            print("Error al actualizar empleado:", e)
            conn.rollback()
        finally:
            conn.close()

    def eliminar_empleado(self, id_empleado):
        conn = self.db.conectar()
        cursor = conn.cursor()
        try:
            sql = "CALL sp_eliminar_empleado(%s)"
            cursor.execute(sql, (id_empleado,))
            conn.commit()
            print("Empleado eliminado")
        except Exception as e:
            print("Error al eliminar empleado:", e)
            conn.rollback()
        finally:
            conn.close()


    def menu_empleado(self):
        while True:
            print("\n--- CRUD Empleado ---")
            print("1. Añadir empleado")
            print("2. Consultar empleados")
            print("3. Editar empleado")
            print("4. Eliminar empleado")
            print("0. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            match opcion:
                case "1":
                    print("\n--- Crear Empleado ---")
                    try:
                        nombre = input("Nombre del empleado: ")
                        fecha_str = input("Fecha de ingreso (YYYY-MM-DD): ")
                        fecha_ingreso = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
                        salario = float(input("Salario mensual: "))
                        telefono = input("Número de teléfono: ")
                        id_servicio = int(input("ID del servicio asociado: "))
                        self.crear_empleado(nombre, fecha_ingreso, salario, telefono, id_servicio)
                    except ValueError:
                        print("Entrada inválida. Verifica los datos.")

                case "2":
                    print("\n--- Mostrar Empleado ---")
                    try:
                        id_empleado = int(input("ID del empleado: "))
                        self.mostrar_empleado(id_empleado)
                    except ValueError:
                        print("ID inválido.")

                case "3":
                    print("\n--- Actualizar Empleado ---")
                    try:
                        id_empleado = int(input("ID del empleado: "))
                        nuevo_servicio = input("Nuevo servicio: ")
                        self.actualizar_empleado(id_empleado, nuevo_servicio)
                    except ValueError:
                        print("ID inválido.")

                case "4":
                    print("\n--- Eliminar Empleado ---")
                    try:
                        id_empleado = int(input("ID del empleado a eliminar: "))
                        confirmacion = input("¿Estás seguro? (s/n): ")
                        if confirmacion.lower() == "s":
                            self.eliminar_empleado(id_empleado)
                        else:
                            print("Eliminación cancelada.")
                    except ValueError:
                        print("ID inválido.")

                case "0":
                    print("Volviendo al menú principal...")
                    break

                case _:
                    print("Opción inválida. Intente de nuevo.")
