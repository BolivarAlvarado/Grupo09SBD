from db_connection import DBConnection

class EmpleadoCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_empleado(self, nombre, fecha_ingreso, salario_mensual, num_telefono, id_servicio):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO Empleado (nombre_emp, fecha_ingreso_emp, salario_mensual, num_telefono, idServicio) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, fecha_ingreso, salario_mensual, num_telefono, id_servicio)
        cursor.execute(sql, valores)
        conn.commit()
        print("Empleado creado.")
        conn.close()

    def mostrar_empleado(self, id_empleado):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM Empleado WHERE idEmpleado = %s"
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
        sql = "UPDATE Empleado SET idServicio = %s WHERE idEmpleado = %s"
        valores = (nuevo_servicio, id_empleado)
        cursor.execute(sql, valores)
        conn.commit()
        print("Empleado actualizado.")
        conn.close()

    def eliminar_empleado(self, id_empleado):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM Empleado WHERE idEmpleado = %s"
        cursor.execute(sql, (id_empleado,))
        conn.commit()
        print("Empleado eliminado.")
        conn.close()
