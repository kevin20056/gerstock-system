from src.models.modelo import datos, guardar, buscar, ahora


def login(usuario, clave):
    u = buscar("usuarios", "usuario", usuario)
    if u and u["clave"] == clave:
        return u
    return None


def crear_usuario(usuario, clave, rol):
    if buscar("usuarios", "usuario", usuario):
        return "Ese usuario ya existe"
    if rol not in ("administrador", "gerente", "colaborador"):
        return "Rol no válido"
    datos["usuarios"].append({"usuario": usuario, "clave": clave, "rol": rol})
    guardar()
    return "Usuario creado"


def registrar_producto(nombre, cantidad, costo):
    if buscar("productos", "nombre", nombre):
        return "El producto ya existe"
    if cantidad < 0 or costo < 0:
        return "Datos no válidos"
    datos["productos"].append({"nombre": nombre, "cantidad": cantidad, "costo": costo})
    guardar()
    return "Producto registrado"


def modificar_producto(nombre, cantidad, costo):
    p = buscar("productos", "nombre", nombre)
    if not p:
        return "El producto no existe"
    if cantidad < 0 or costo < 0:
        return "Datos no válidos"
    p["cantidad"] = cantidad
    p["costo"] = costo
    guardar()
    return "Producto modificado"


def eliminar_producto(nombre):
    p = buscar("productos", "nombre", nombre)
    if not p:
        return "El producto no existe"
    datos["productos"].remove(p)
    guardar()
    return "Producto eliminado"


def movimiento(nombre, tipo, cantidad, usuario):
    p = buscar("productos", "nombre", nombre)
    if not p:
        return "El producto no existe"
    if tipo not in ("entrada", "salida") or cantidad <= 0:
        return "Datos no válidos"
    if tipo == "salida" and cantidad > p["cantidad"]:
        return "Solo hay " + str(p["cantidad"]) + " disponibles"
    if tipo == "entrada":
        p["cantidad"] += cantidad
    else:
        p["cantidad"] -= cantidad
    datos["movimientos"].append({"producto": nombre, "tipo": tipo, "cantidad": cantidad,
                                 "usuario": usuario, "fecha": ahora()})
    guardar()
    return "Movimiento registrado"


def registrar_equipo(codigo, ubicacion):
    if buscar("equipos", "codigo", codigo):
        return "El equipo ya existe"
    datos["equipos"].append({"codigo": codigo, "ubicacion": ubicacion, "historial": []})
    guardar()
    return "Equipo registrado"


def mover_equipo(codigo, ubicacion, usuario):
    e = buscar("equipos", "codigo", codigo)
    if not e:
        return "El equipo no existe"
    if e["ubicacion"] == ubicacion:
        return "La ubicación debe ser distinta"
    e["historial"].append({"desde": e["ubicacion"], "hasta": ubicacion,
                           "usuario": usuario, "fecha": ahora()})
    e["ubicacion"] = ubicacion
    guardar()
    return "Equipo movido"


def calcular_costo(materiales, otros):
    """materiales: lista de (nombre, cantidad). Devuelve el total o None si hay error."""
    total = otros
    for nombre, cantidad in materiales:
        p = buscar("productos", "nombre", nombre)
        if not p or cantidad <= 0:
            return None
        total += p["costo"] * cantidad
    return total


def asignar_tarea(descripcion, responsable):
    u = buscar("usuarios", "usuario", responsable)
    if not u or u["rol"] != "colaborador":
        return "El responsable debe ser un colaborador"
    datos["tareas"].append({"descripcion": descripcion, "responsable": responsable})
    guardar()
    return "Tarea asignada"


def tareas_de(user):
    if user["rol"] == "colaborador":
        return [t for t in datos["tareas"] if t["responsable"] == user["usuario"]]
    return datos["tareas"]