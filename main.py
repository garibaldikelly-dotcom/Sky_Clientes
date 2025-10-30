import sys
import os

# para poder importar sky_app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from sky_app import crear_cliente, modificar_cliente, consultar_cliente, listar_clientes
except ImportError:
    print("❌ ERROR: No se pudo importar sky_app.py.")
    print("Asegúrate de que sky_app.py esté en el mismo directorio.")
    sys.exit(1)

def mostrar_menu():
    """Muestra las opciones del menú."""
    print("\n" + "=" * 40)
    print("  MENÚ DE GESTIÓN DE CLIENTES (SKY APP)")
    print("=" * 40)
    print("1. Crear nuevo cliente")
    print("2. Modificar servicio de cliente")
    print("3. Consultar información de cliente")
    print("4. Listar todos los clientes")
    print("5. Salir")
    print("-" * 40)

def obtener_nombre_cliente():
    """Pide y retorna el nombre del cliente con validación básica."""
    while True:
        nombre = input("▶️  Ingrese el nombre del cliente: ").strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío.")

def main():
    """Función principal para la ejecución del menú."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == '1':
            ## CREAR CLIENTE
            print("\n--- CREAR CLIENTE ---")
            nombre = obtener_nombre_cliente()
            servicio = input("Ingrese el servicio inicial: ")
            crear_cliente(nombre, servicio)

        elif opcion == '2':
            ## MODIFICAR CLIENTE
            print("\n--- MODIFICAR CLIENTE ---")
            nombre = obtener_nombre_cliente()
            nuevo_servicio = input("Ingrese el nuevo servicio o descripción a añadir: ")
            modificar_cliente(nombre, nuevo_servicio)

        elif opcion == '3':
            ## CONSULTAR CLIENTE
            print("\n--- CONSULTAR CLIENTE ---")
            nombre = obtener_nombre_cliente()
            consultar_cliente(nombre)

        elif opcion == '4':
            ## LISTAR CLIENTES
            print("\n--- LISTADO ---")
            listar_clientes()

        elif opcion == '5':
            ## SALIR
            print("\n👋 ¡Gracias por usar la aplicación de gestión de clientes! Saliendo...")
            break

        else:
            print("❌ Opción no válida. Por favor, ingrese un número del 1 al 5.")

# El punto de entrada del script
if __name__ == "__main__":
    main()