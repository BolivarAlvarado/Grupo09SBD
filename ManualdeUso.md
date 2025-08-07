# **Manual de Usuario - Sistema Integrado de Gestión Muebles para Empresa MUARTE**

## **1. Propósito del Sistema**
Este sistema de datos combina la gestión de clientes, proveedores, servicios, reportes de avance, transportistas, pedidos y pagos para la empresa MUARTE de tapizado, lacado, diseño y venta de muebles. También mejora la logística de entrega desde el taller al cliente, al hacer más eficiente los tiempos operativos por medio de usar una base de sistema de datos.

## **2. Instalación y Entorno**
Asegúrate de tener instalado **Python** y el módulo **mysql.connector**.

Las conexiones se realizan mediante esta configuración en la clase `DBConnection`:

```python
self.host = "0.tcp.sa.ngrok.io"
self.port = 18480
self.user = "adminmuarte"
self.password = "awp2210S@"
self.database = "muarteDB"
```


## **3. Estructura y Navegación del Menú Principal**
Al iniciar la aplicación, verás el siguiente menú principal:



### **Menú Principal**

1. **Cliente**
2. **Proveedor**
3. **Servicio**
4. **Reporte de Avance**
5. **Transportista**
6. **Pedido**
7. **Pago**
0. **Salir**


## **4. Uso de Cada Menú CRUD**
Cada uno de los módulos (Cliente, Proveedor, etc.) sigue esta estructura estándar:



### **CRUD [Nombre del Módulo]**

1. **Añadir [entidad]**
2. **Consultar [entidad]**
3. **Editar [campo clave]**
4. **Eliminar [entidad]**
0. **Volver al menú pri**


### **Detalle de operaciones:**

- **Añadir**: Da de alta un registro. Se solicitarán campos como nombre, fechas, estado, id vinculado, etc.
- **Consultar**: Pregunta por ID único y muestra la información si existe.
- **Editar**: Solicita un ID y un campo a modificar (por ejemplo, correo, precio, estado).
- **Eliminar**: Pregunta por ID, solicita confirmación (s/n) y elimina si se confirma.
- **Volver**: Regresa al menú principal.















## Diagrama Lógico
<img width="1637" height="1131" alt="image" src="https://github.com/user-attachments/assets/ec1f4454-97c7-4f37-bb68-a5ef57c7ecf7" />

