import json
import os
from datetime import datetime

ARCHIVO = "data.json"
datos = {"usuarios": [{"usuario": "admin", "clave": "1234", "rol": "administrador"}],
         "productos": [], "equipos": [], "movimientos": [], "tareas": []}

if os.path.exists(ARCHIVO):
    with open(ARCHIVO) as f:
        datos = json.load(f)


def guardar():
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=2)


def buscar(lista, campo, valor):
    for x in datos[lista]:
        if x[campo] == valor:
            return x
    return None


def ahora():
    return datetime.now().strftime("%Y-%m-%d %H:%M")