import os

# Define la ruta del directorio de datos
DATA_DIR = "data"

def inicializar_directorio():
    """Asegura que el directorio 'data' exista."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"Directorio '{DATA_DIR}/' creado.")

def obtener_ruta_archivo(nombre):
    """Retorna la ruta completa del archivo de un cliente."""
    return os.path.join(DATA_DIR, f"{nombre}.txt")

def crear_cliente(nombre, servicio):
    """
    Crea un archivo (data/nombre.txt) con la información inicial del cliente.
    """
    inicializar_directorio()
    ruta_archivo = obtener_ruta_archivo(nombre)

    if os.path.exists(ruta_archivo):
        print(f"⚠️ Error: El cliente '{nombre}' ya existe.")
        return

    try:
        with open(ruta_archivo, 'w') as f:
            f.write(f"--- Cliente: {nombre} ---\n")
            f.write(f"Servicio inicial: {servicio}\n")
        print(f"✅ Cliente '{nombre}' creado con el servicio '{servicio}'.")
    except IOError as e:
        print(f"❌ Error al crear el archivo para '{nombre}': {e}")

def modificar_cliente(nombre, nuevo_servicio):
    """
    Busca el archivo y agrega la descripción del nuevo servicio.
    """
    ruta_archivo = obtener_ruta_archivo(nombre)

    if not os.path.exists(ruta_archivo):
        print(f"⚠️ Error: El cliente '{nombre}' no se encontró.")
        return

    try:
        with open(ruta_archivo, 'a') as f:
            f.write(f"--- Modificación ---\n")
            f.write(f"Nuevo servicio añadido: {nuevo_servicio}\n")
        print(f"📝 Servicio '{nuevo_servicio}' añadido al cliente '{nombre}'.")
    except IOError as e:
        print(f"❌ Error al modificar el archivo para '{nombre}': {e}")

def consultar_cliente(nombre):
    """
    Lee y muestra el contenido del archivo de un cliente.
    """
    ruta_archivo = obtener_ruta_archivo(nombre)

    if not os.path.exists(ruta_archivo):
        print(f"⚠️ Error: El cliente '{nombre}' no se encontró.")
        return

    try:
        with open(ruta_archivo, 'r') as f:
            contenido = f.read()
            print(f"\n--- Contenido del Archivo de {nombre} ---")
            print(contenido)
            print("-------------------------------------------\n")
    except IOError as e:
        print(f"❌ Error al leer el archivo para '{nombre}': {e}")

def listar_clientes():
    """
    Lista los archivos (.txt) en el directorio data/.
    """
    inicializar_directorio()
    archivos = [f for f in os.listdir(DATA_DIR) if f.endswith(".txt")]

    if not archivos:
        print(f"ℹ️ No se encontraron clientes en el directorio '{DATA_DIR}/'.")
        return

    print("\n--- Listado de Clientes ---")
    for i, archivo in enumerate(archivos, 1):
        # Elimina la extensión '.txt' para mostrar solo el nombre del cliente
        nombre_cliente = os.path.splitext(archivo)[0]
        print(f"{i}. {nombre_cliente}")
    print("-----------------------------\n")