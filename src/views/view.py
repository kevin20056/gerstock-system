from src.controllers import controller as c
from src.models.modelo import datos

ADM, GER, COL = "administrador", "gerente", "colaborador"

# opción: roles que pueden usarla
PERMISOS = {"1": [ADM], "2": [GER, COL], "3": [ADM, GER, COL], "4": [ADM, GER, COL],
            "5": [ADM, GER, COL], "6": [GER, COL], "7": [GER, COL], "8": [GER, COL],
            "9": [GER], "10": [GER], "11": [GER, COL], "12": [GER], "13": [GER]}


def numero(texto):
    try:
        return float(input(texto))
    except ValueError:
        return -1


def iniciar():
    print("=== GERSTOCK ===")
    user = c.login(input("Usuario: "), input("Clave: "))
#Ev
    if user:
        menu(user)
    else:
        print("Usuario o clave incorrectos")


def menu(user):
    while True:
        print("\n1 Crear usuario | 2 Registrar producto | 3 Ver productos")
        print("4 Entrada/salida | 5 Ver movimientos | 6 Registrar equipo")
        print("7 Mover equipo | 8 Ver equipos | 9 Calcular costo")
        print("10 Asignar tarea | 11 Ver tareas | 12 Modificar producto")
        print("13 Eliminar producto | 0 Salir")
        op = input("Opción: ")
        if op == "0":
            break
        if op not in PERMISOS:
            print("Opción no válida")
        elif user["rol"] not in PERMISOS[op]:
            print("No tiene permiso para esta opción")
        elif op == "1":
            print(c.crear_usuario(input("Usuario: "), input("Clave: "), input("Rol (administrador/gerente/colaborador): ")))
        elif op == "2":
            print(c.registrar_producto(input("Nombre: "), numero("Cantidad: "), numero("Costo unitario: ")))
        elif op == "3":
            for p in datos["productos"]:
                print("-", p["nombre"], "| cantidad:", p["cantidad"], "| costo:", p["costo"])
        elif op == "4":
            print(c.movimiento(input("Producto: "), input("Tipo (entrada/salida): "), numero("Cantidad: "), user["usuario"]))
        elif op == "5":
            for m in datos["movimientos"]:
                print("-", m["fecha"], m["tipo"], m["cantidad"], m["producto"], "por", m["usuario"])
        elif op == "6":
            print(c.registrar_equipo(input("Código: "), input("Ubicación: ")))
        elif op == "7":
            print(c.mover_equipo(input("Código: "), input("Nueva ubicación: "), user["usuario"]))
        elif op == "8":
            for e in datos["equipos"]:
                print("-", e["codigo"], "| ubicación:", e["ubicacion"])
        elif op == "9":
            materiales = []
            while True:
                nombre = input("Material (enter para terminar): ")
                if nombre == "":
                    break
                materiales.append((nombre, numero("Cantidad usada: ")))
            total = c.calcular_costo(materiales, numero("Otros costos (mano de obra, transporte): "))
            print("Datos no válidos" if total is None or total < 0 else "Costo total: " + str(total))
        elif op == "10":
            print(c.asignar_tarea(input("Descripción: "), input("Colaborador responsable: ")))
        elif op == "11":
            for t in c.tareas_de(user):
                print("-", t["descripcion"], "|", t["responsable"])
        elif op == "12":
            print(c.modificar_producto(input("Producto: "), numero("Nueva cantidad: "), numero("Nuevo costo: ")))
        elif op == "13":
            print(c.eliminar_producto(input("Producto: ")))