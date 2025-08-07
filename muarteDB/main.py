from Cliente import ClienteCRUD
from Empleado import EmpleadoCRUD
from Material import MaterialCRUD
from Pago import PagoCRUD
from Pedido import PedidoCRUD
from Proveedor import ProveedorCRUD
from ReporteAvance import ReporteAvanceCRUD
from Servicio import ServicioCRUD
from Transportista import TransportistaCRUD

def menu_principal():
  while True:
        print("\n--- Menú Principal ---")
        print("1. Cliente")
        print("2. Empleado")
        print("3. Material")
        print("4. Pago")
        print("5. Pedido")
        print("6. Proveedor")
        print("7. Reporte de Avance")
        print("8. Servicio")
        print("9. Transportista")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                cliente = ClienteCRUD()
                cliente.menu_cliente()
            case "2":
                empleado = EmpleadoCRUD()
                empleado.menu_empleado()
            case "3":
                material = MaterialCRUD()
                material.menu_material()
            case "4":
                pago = PagoCRUD()
                pago.menu_pago()
            case "5":
                pedido = PedidoCRUD()
                pedido.menu_pedido()
            case "6":
                proveedor = ProveedorCRUD()
                proveedor.menu_proveedor()
            case "7":
                reporte_crud = ReporteAvanceCRUD()
                reporte_crud.menu_reporte_avance()
            case "8":
                servicio = ServicioCRUD()
                servicio.menu_servicio()
            case "9":
                transportista = TransportistaCRUD()
                transportista.menu_transportista()
            case "0":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()
  

# Pruebas
#cliente.crear_cliente("Av. Central", "Luis Perez", "099999999", "luis@gmail.com")
#cliente.mostrar_cliente(1)
#cliente.actualizar_cliente(1, "nuevo@email.com")
#cliente.eliminar_cliente(1)

