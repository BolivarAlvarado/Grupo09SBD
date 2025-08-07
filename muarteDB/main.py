from Cliente import menu_cliente
from Empleado import menu_empleado
from Material import menu_material
from Pago import menu_pago
from Pedido import menu_pedido
from Proveedor import menu_proveedor
from ReporteAvance import menu_reporte_avance
from Servicio import menu_servicio
from Transportista import menu_transportista

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
                menu_cliente()
            case "2":
                menu_empleado()
            case "3":
                menu_material()
            case "4":
                menu_pago()
            case "5":
                menu_pedido()
            case "6":
                menu_proveedor()
            case "7":
                menu_reporte_avance()
            case "8":
                menu_servicio()
            case "9":
                menu_transportista()
            case "0":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    main()
  

# Pruebas
#cliente.crear_cliente("Av. Central", "Luis Perez", "099999999", "luis@gmail.com")
#cliente.mostrar_cliente(1)
#cliente.actualizar_cliente(1, "nuevo@email.com")
#cliente.eliminar_cliente(1)

