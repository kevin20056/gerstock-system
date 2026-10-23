import json
# Para interactuar con el sistema operativo
import os
from datetime import datetime

ARCHIVO = "data.json"
datos = {"usuarios": [{"usuario": "admin", "clave": "1234", "rol": "administrador"}],
         "productos": [], "equipos": [], "movimientos": [], "tareas": []}

# Lee
if os.path.exists(ARCHIVO):
    with open(ARCHIVO) as f:
        datos = json.load(f)

#Escribe 
def guardar():
    with open(ARCHIVO, "w") as f:
#Escribe ar, ordena
        json.dump(datos, f, indent=2)


def buscar(lista, campo, valor):
    for x in datos[lista]:
#Compara 
        if x[campo] == valor:
            return x
    return None

# CO - H
def ahora():
    return datetime.now().strftime("%Y-%m-%d %H:%M")