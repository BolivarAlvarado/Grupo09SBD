from db_connection import DBConnection

class PedidoCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_pedido(self, fotoEntrega, fechaEntrega, fechaInicio, estado_pedido, id_cliente, id_transportista):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO Pedido (fotoEntrega, fechaEntrega, fechaInicio, estadoPedido, idCliente, idTransportista) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (fotoEntrega, fechaEntrega, fechaInicio, estado_pedido, id_cliente, id_transportista)
        cursor.execute(sql, valores)
        conn.commit()
        print("Pedido creado.")
        conn.close()

    def mostrar_pedido(self, id_pedido):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM Pedido WHERE idPedido = %s"
        cursor.execute(sql, (id_pedido,))
        resultado = cursor.fetchone()
        if resultado:
            print("Pedido encontrado:", resultado)
        else:
            print("Pedido no encontrado.")
        conn.close()

    def actualizar_pedido(self, id_pedido, nuevo_estado):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "UPDATE Pedido SET estadoPedido = %s WHERE idPedido = %s"
        valores = (nuevo_estado, id_pedido)
        cursor.execute(sql, valores)
        conn.commit()
        print("Pedido actualizado.")
        conn.close()

    def eliminar_pedido(self, id_pedido):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM Pedido WHERE idPedido = %s"
        cursor.execute(sql, (id_pedido,))
        conn.commit()
        print("Pedido eliminado.")
        conn.close()
        
    def menu_pedido(self):
        while True:
            print("\n--- CRUD Pedido ---")
            print("1. Añadir pedido")
            print("2. Consultar pedido")
            print("3. Editar estado del pedido")
            print("4. Eliminar pedido")
            print("0. Volver al menú principal")
    
            opcion = input("Seleccione una opción: ")
    
            match opcion:
                case "1":
                    print("\n--- Crear Pedido ---")
                    foto_entrega = input("Ruta o nombre de la foto de entrega: ")
                    fecha_entrega = input("Fecha de entrega (YYYY-MM-DD): ")
                    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
                    estado_pedido = input("Estado del pedido: ")
                    try:
                        id_cliente = int(input("ID del cliente: "))
                        id_transportista = int(input("ID del transportista: "))
                        pedido_crud.crear_pedido(foto_entrega, fecha_entrega, fecha_inicio, estado_pedido, id_cliente, id_transportista)
                    except ValueError:
                        print("ID inválido.")
    
                case "2":
                    print("\n--- Mostrar Pedido ---")
                    try:
                        id_pedido = int(input("ID del pedido: "))
                        pedido_crud.mostrar_pedido(id_pedido)
                    except ValueError:
                        print("ID inválido.")
    
                case "3":
                    print("\n--- Actualizar Estado del Pedido ---")
                    try:
                        id_pedido = int(input("ID del pedido: "))
                        nuevo_estado = input("Nuevo estado del pedido: ")
                        pedido_crud.actualizar_pedido(id_pedido, nuevo_estado)
                    except ValueError:
                        print("ID inválido.")
    
                case "4":
                    print("\n--- Eliminar Pedido ---")
                    try:
                        id_pedido = int(input("ID del pedido a eliminar: "))
                        confirmacion = input("¿Estás seguro? (s/n): ")
                        if confirmacion.lower() == "s":
                            pedido_crud.eliminar_pedido(id_pedido)
                        else:
                            print("Eliminación cancelada.")
                    except ValueError:
                        print("ID inválido.")
    
                case "0":
                    print("Volviendo al menú principal...")
                    break
    
                case _:
                    print("Opción inválida. Intente de nuevo.")
    
