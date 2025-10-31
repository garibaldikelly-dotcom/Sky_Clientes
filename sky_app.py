import sys
import os
import json
# CONFIGURACIÓN Y RUTAS
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "clientes.json")

os.makedirs(DATA_DIR, exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=4)
# FUNCIONES DE GESTIÓN DE CLIENTES
def cargar_clientes():
    """Carga los clientes desde el archivo JSON."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_clientes(clientes):
    """Guarda los clientes en el archivo JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)

def crear_cliente(nombre, correo, telefono, servicio):
    """Crea un nuevo cliente y lo guarda en el archivo."""
    clientes = cargar_clientes()
    if nombre in clientes:
        print(f"⚠️ El cliente '{nombre}' ya existe.")
        return
    clientes[nombre] = {
        "correo": correo,
        "telefono": telefono,
        "servicio": servicio
    }
    guardar_clientes(clientes)
    print(f"✅ Cliente '{nombre}' creado correctamente.")

def modificar_cliente(nombre, nuevo_servicio):
    """Modifica el servicio de un cliente existente."""
    clientes = cargar_clientes()
    if nombre not in clientes:
        print(f"❌ El cliente '{nombre}' no existe.")
        return
    clientes[nombre]["servicio"] = nuevo_servicio
    guardar_clientes(clientes)
    print(f"✅ Servicio de '{nombre}' actualizado a '{nuevo_servicio}'.")

def consultar_cliente(nombre):
    """Muestra la información de un cliente."""
    clientes = cargar_clientes()
    if nombre not in clientes:
        print(f"❌ El cliente '{nombre}' no existe.")
        return
    datos = clientes[nombre]
    print("\n📋 Información del cliente:")
    print(f"  Nombre: {nombre}")
    print(f"  Correo: {datos['correo']}")
    print(f"  Teléfono: {datos['telefono']}")
    print(f"  Servicio: {datos['servicio']}")

def listar_clientes():
    """Lista todos los clientes registrados."""
    clientes = cargar_clientes()
    if not clientes:
        print("📂 No hay clientes registrados.")
        return
    print("\n📜 LISTA DE CLIENTES:")
    for nombre, datos in clientes.items():
        print(f"- {nombre} | {datos['correo']} | {datos['telefono']} | Servicio: {datos['servicio']}")

def eliminar_cliente(nombre):
    """Elimina un cliente del registro."""
    clientes = cargar_clientes()
    if nombre not in clientes:
        print(f"❌ El cliente '{nombre}' no existe.")
        return
    del clientes[nombre]
    guardar_clientes(clientes)
    print(f"🗑️ Cliente '{nombre}' eliminado correctamente.")
# INTERFAZ DE MENÚ
def mostrar_menu():
    """Muestra las opciones del menú."""
    print("\n" + "=" * 45)
    print("  MENÚ DE GESTIÓN DE CLIENTES (SKY APP)")
    print("=" * 45)
    print("1. Crear nuevo cliente")
    print("2. Modificar servicio de cliente")
    print("3. Consultar información de cliente")
    print("4. Listar todos los clientes")
    print("5. Eliminar cliente")
    print("6. Salir")
    print("-" * 45)

def obtener_nombre_cliente():
    """Pide y retorna el nombre del cliente con validación básica."""
    while True:
        nombre = input("▶️  Ingrese el nombre del cliente: ").strip()
        if nombre:
            return nombre
        print("❌ El nombre no puede estar vacío.")
# FUNCIÓN PRINCIPAL
def main():
    """Función principal para la ejecución del menú."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == '1':
            print("\n--- CREAR CLIENTE ---")
            nombre = obtener_nombre_cliente()
            correo = input("Ingrese el correo del cliente: ").strip()
            telefono = input("Ingrese el teléfono del cliente: ").strip()
            servicio = input("Ingrese el servicio contratado: ").strip()
            crear_cliente(nombre, correo, telefono, servicio)

        elif opcion == '2':
            print("\n--- MODIFICAR SERVICIO ---")
            nombre = obtener_nombre_cliente()
            nuevo_servicio = input("Ingrese el nuevo servicio: ").strip()
            modificar_cliente(nombre, nuevo_servicio)

        elif opcion == '3':
            print("\n--- CONSULTAR CLIENTE ---")
            nombre = obtener_nombre_cliente()
            consultar_cliente(nombre)

        elif opcion == '4':
            print("\n--- LISTADO DE CLIENTES ---")
            listar_clientes()

        elif opcion == '5':
            print("\n--- ELIMINAR CLIENTE ---")
            nombre = obtener_nombre_cliente()
            eliminar_cliente(nombre)

        elif opcion == '6':
            print("\n👋 ¡Gracias por usar la aplicación de gestión de clientes! Saliendo...")
            break

        else:
            print("❌ Opción no válida. Por favor, ingrese un número del 1 al 6.")

# PUNTO DE ENTRADA
if __name__ == "__main__":
    main()
