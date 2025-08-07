from db_connection import DBConnection

class ServicioCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_servicio(self,precio_base, descripcion, tipo_danio, estado_mueble,foto_disenio, nombre_disenio, estilo, tipo_mueble, duracion_estimada):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = """
            INSERT INTO Servicio (precio_base, descripcion, tipo_danio, estado_Mueble, foto_disenio, nombreDisenio, estilo, tipoMueble, duracionEstimada)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
          """
        valores = (precio_base, descripcion, tipo_danio, estado_mueble,foto_disenio, nombre_disenio, estilo, tipo_mueble, duracion_estimada)
        cursor.execute(sql, valores)
        conn.commit()
        print("Servicio creado.")
        conn.close()

    def mostrar_servicio(self, id_servicio):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM Servicio WHERE idServicio = %s"
        cursor.execute(sql, (id_servicio,))
        resultado = cursor.fetchone()
        if resultado:
            print("Servicio encontrado:", resultado)
        else:
            print("Servicio no encontrado.")
        conn.close()

    def actualizar_servicio(self, id_servicio, nuevo_costo):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "UPDATE Servicio SET precio_base = %s WHERE idServicio = %s"
        valores = (nuevo_costo, id_servicio)
        cursor.execute(sql, valores)
        conn.commit()
        print("Servicio actualizado.")
        conn.close()

    def eliminar_servicio(self, id_servicio):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM Servicio WHERE idServicio = %s"
        cursor.execute(sql, (id_servicio,))
        conn.commit()
        print("Servicio eliminado.")
        conn.close()
    def menu_servicio():
        servicio_crud = ServicioCRUD()
    
        while True:
            print("\n--- CRUD Servicio ---")
            print("1. Añadir servicio")
            print("2. Consultar servicio")
            print("3. Editar precio del servicio")
            print("4. Eliminar servicio")
            print("0. Volver al menú principal")
    
            opcion = input("Seleccione una opción: ")
    
            match opcion:
                case "1":
                    print("\n--- Crear Servicio ---")
                    try:
                        precio_base = float(input("Precio base: "))
                        descripcion = input("Descripción: ")
                        tipo_danio = input("Tipo de daño: ")
                        estado_mueble = input("Estado del mueble: ")
                        foto_disenio = input("Ruta o nombre de la foto del diseño: ")
                        nombre_disenio = input("Nombre del diseño: ")
                        estilo = input("Estilo: ")
                        tipo_mueble = input("Tipo de mueble: ")
                        duracion_estimada = input("Duración estimada: ")
                        servicio_crud.crear_servicio(precio_base, descripcion, tipo_danio, estado_mueble, foto_disenio, nombre_disenio, estilo, tipo_mueble, duracion_estimada)
                    except ValueError:
                        print("Precio inválido.")
    
                case "2":
                    print("\n--- Mostrar Servicio ---")
                    try:
                        id_servicio = int(input("ID del servicio: "))
                        servicio_crud.mostrar_servicio(id_servicio)
                    except ValueError:
                        print("ID inválido.")
    
                case "3":
                    print("\n--- Actualizar Precio del Servicio ---")
                    try:
                        id_servicio = int(input("ID del servicio: "))
                        nuevo_costo = float(input("Nuevo precio base: "))
                        servicio_crud.actualizar_servicio(id_servicio, nuevo_costo)
                    except ValueError:
                        print("Datos inválidos.")
    
                case "4":
                    print("\n--- Eliminar Servicio ---")
                    try:
                        id_servicio = int(input("ID del servicio a eliminar: "))
                        confirmacion = input("¿Estás seguro? (s/n): ")
                        if confirmacion.lower() == "s":
                            servicio_crud.eliminar_servicio(id_servicio)
                        else:
                            print("Eliminación cancelada.")
                    except ValueError:
                        print("ID inválido.")
    
                case "0":
                    print("Volviendo al menú principal...")
                    break
    
                case _:
                    print("Opción inválida. Intente de nuevo.")
    
