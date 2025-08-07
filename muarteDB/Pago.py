from db_connection import DBConnection

class PagoCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_pago(self, metodo_pago, fecha_pago, descuento, subtotal, iva, monto_pago, id_pedido):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO Pago (metodoPago, fechaPago, descuento, subtotal, iva, montoPago, idPedido) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (metodo_pago, fecha_pago, descuento, subtotal, iva, monto_pago, id_pedido)
        cursor.execute(sql, valores)
        conn.commit()
        print("Pago registrado.")
        conn.close()

    def mostrar_pago(self, id_pago):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM Pago WHERE idPago = %s"
        cursor.execute(sql, (id_pago,))
        resultado = cursor.fetchone()
        if resultado:
            print("Pago encontrado:", resultado)
        else:
            print("Pago no encontrado.")
        conn.close()

    def actualizar_pago(self, id_pago, nuevo_total):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "UPDATE Pago SET montoPago = %s WHERE idPago = %s"
        valores = (nuevo_total, id_pago)
        cursor.execute(sql, valores)
        conn.commit()
        print("Pago actualizado.")
        conn.close()

    def eliminar_pago(self, id_pago):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM Pago WHERE idPago = %s"
        cursor.execute(sql, (id_pago,))
        conn.commit()
        print("Pago eliminado.")
        conn.close()
    
    def menu_pago(self):
        while True:
            print("\n--- CRUD Pago ---")
            print("1. Registrar pago")
            print("2. Consultar pago")
            print("3. Editar monto del pago")
            print("4. Eliminar pago")
            print("0. Volver al menú principal")
    
            opcion = input("Seleccione una opción: ")
    
            match opcion:
                case "1":
                    print("\n--- Registrar Pago ---")
                    metodo_pago = input("Método de pago: ")
                    fecha_pago = input("Fecha del pago (YYYY-MM-DD): ")
                    try:
                        descuento = float(input("Descuento: "))
                        subtotal = float(input("Subtotal: "))
                        iva = float(input("IVA: "))
                        monto_pago = float(input("Monto total a pagar: "))
                        id_pedido = int(input("ID del pedido: "))
                        pago_crud.crear_pago(metodo_pago, fecha_pago, descuento, subtotal, iva, monto_pago, id_pedido)
                    except ValueError:
                        print("Datos numéricos inválidos.")
    
                case "2":
                    print("\n--- Mostrar Pago ---")
                    try:
                        id_pago = int(input("ID del pago: "))
                        pago_crud.mostrar_pago(id_pago)
                    except ValueError:
                        print("ID inválido.")
    
                case "3":
                    print("\n--- Actualizar Monto del Pago ---")
                    try:
                        id_pago = int(input("ID del pago: "))
                        nuevo_total = float(input("Nuevo monto del pago: "))
                        pago_crud.actualizar_pago(id_pago, nuevo_total)
                    except ValueError:
                        print("Datos inválidos.")
    
                case "4":
                    print("\n--- Eliminar Pago ---")
                    try:
                        id_pago = int(input("ID del pago a eliminar: "))
                        confirmacion = input("¿Estás seguro? (s/n): ")
                        if confirmacion.lower() == "s":
                            pago_crud.eliminar_pago(id_pago)
                        else:
                            print("Eliminación cancelada.")
                    except ValueError:
                        print("ID inválido.")
    
                case "0":
                    print("Volviendo al menú principal...")
                    break
    
                case _:
                    print("Opción inválida. Intente de nuevo.")
    
