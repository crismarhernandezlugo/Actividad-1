import json
import os

# Ruta donde se guardarán los datos
# Pydroid creará la carpeta data automáticamente si sigues este código
RUTA_DB = "data/inventario.json"

def guardar_json(datos):
    # Asegura que la carpeta data exista
    if not os.path.exists("data"):
        os.makedirs("data")
    with open(RUTA_DB, "w") as f:
        json.dump(datos, f, indent=4)

def cargar_json():
    if not os.path.exists(RUTA_DB):
        return []
    try:
        with open(RUTA_DB, "r") as f:
            return json.load(f)
    except:
        return []
