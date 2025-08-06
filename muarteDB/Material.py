from db_connection import DBConnection
from datetime import datetime

class MaterialCRUD:
    def __init__(self):
        self.db = DBConnection()

    def crear_material(self, descripcion, stock, color, tipo_material, costo_material, stock_minimo, id_proveedor):
        conn = self.db.conectar()
        cursor = conn.cursor()

        fecha_ingreso = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        sql = """
            INSERT INTO Material (descripcion, stock, color, tipoMaterial, costoMaterial, fechaIngreso, stockMinimo, idProveedor)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
        valores = (descripcion, stock, color, tipo_material, costo_material, fecha_ingreso, stock_minimo, id_proveedor)

        cursor.execute(sql, valores)
        conn.commit()
        print("Material creado.")
        conn.close()

    def mostrar_material(self, id_material):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "SELECT * FROM Material WHERE idMaterial = %s"
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
        sql = "UPDATE Material SET costoMaterial = %s WHERE idMaterial = %s"
        valores = (nuevo_costo, id_material)
        cursor.execute(sql, valores)
        conn.commit()
        print("Material actualizado.")
        conn.close()

    def eliminar_material(self, id_material):
        conn = self.db.conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM Material WHERE idMaterial = %s"
        cursor.execute(sql, (id_material,))
        conn.commit()
        print("Material eliminado.")
        conn.close()
