# Taller 5 · Diagrama de clases

- **Entrega:** en el **repositorio del equipo en GitHub**, diligenciando el enunciado con los puntos 2, 3 y 4 y subiendo el diagrama al repositorio _(imagen exportada o fuente PlantUML/draw.io)_.
- **Requisito previo:** diagrama de casos de uso del Taller 4.
- Herramienta: draw.io, PlantUML, StarUML o Visual Paradigm.

---

## 1. Guía mínima

**Diagrama de clases:** vista estructural del sistema. Muestra qué cosas existen en el dominio, qué datos guardan, qué saben hacer y cómo se relacionan. No muestra orden ni tiempo: eso es de los diagramas de secuencia.

### Clase

```bash
┌──────────────────────┐
│       Turno          │  ← nombre: sustantivo singular, del vocabulario del dominio
├──────────────────────┤
│ - fecha: Fecha       │  ← atributos: visibilidad nombre: tipo
│ - estado: EstadoTurno│
├──────────────────────┤
│ + cancelar(): void   │  ← métodos: visibilidad nombre(parámetros): retorno
└──────────────────────┘
```

- **Visibilidad:** `+` pública, `-` privada, `#` protegida, `~` de paquete. Los atributos van privados por defecto.
- En el **modelo de dominio** se pueden omitir los métodos: importan los conceptos, sus datos y sus relaciones.
- Una clase **no es una pantalla, una tabla ni un botón**. `PantallaLogin` o `BotonGuardar` no son conceptos del dominio.

### Relaciones

| Relación        | Notación                                  | Se lee                           | Ejemplo                  |
| --------------- | ----------------------------------------- | -------------------------------- | ------------------------ |
| **Asociación**  | línea simple                              | "A se relaciona con B"           | Cliente — Turno          |
| **Agregación**  | rombo vacío en el todo                    | "A tiene B, pero B existe sin A" | Barbería ◇— Barbero      |
| **Composición** | rombo lleno en el todo                    | "B es parte de A y muere con A"  | Factura ◆— LíneaFactura  |
| **Herencia**    | flecha con triángulo vacío hacia el padre | "B es un tipo de A"              | Usuario ◁— Administrador |
| **Dependencia** | flecha punteada                           | "A usa a B de paso"              | Reporte ⇢ Turno          |

- Ante la duda entre agregación y composición: si al borrar el todo **las partes no tienen sentido solas**, es composición.
- Herencia solo si el hijo **es un** padre y comparte su comportamiento. Si solo comparten un campo, no es herencia.

### Multiplicidad

Se escribe en cada extremo de la relación: cuántos objetos de ese lado se relacionan con **uno** del otro.

| Notación     | Significa       |
| ------------ | --------------- |
| `1`          | exactamente uno |
| `0..1`       | cero o uno      |
| `*` o `0..*` | cero o muchos   |
| `1..*`       | uno o muchos    |

- `Cliente 1 —— 0..* Turno`: un cliente tiene cero o muchos turnos; cada turno es de exactamente un cliente.
- Una relación sin multiplicidad está incompleta.

### Navegabilidad

- Flecha abierta en un extremo: desde A se llega a B, pero no al revés.
- En el modelo de dominio se puede dejar sin flecha _(bidireccional)_; se decide en el diseño.

### Cómo encontrar las clases

1. Subrayar los **sustantivos** del catálogo de requisitos y de las descripciones de los casos de uso.
2. Descartar sinónimos, atributos disfrazados _(el "nombre" no es una clase)_, actores que no guardan datos y cosas fuera del alcance.
3. Lo que queda son **clases candidatas**. Los **verbos** entre ellas sugieren relaciones.

---

## 2. Clases candidatas

| Clase candidata          | Fuente _(RF o caso de uso)_                                                 | ¿Se queda?      | Por qué                                                                                                               |
| ------------------------ | --------------------------------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------- |
| _(completar)_            | _(RF-0#, CU-0#)_                                                            | Sí / No         | _(completar)_                                                                                                         |
| Empresa                  | Encuesta del proyecto, respuesta 1; RF-10, CU-09 _(por confirmar)_          | Sí, provisional | En la encuesta se plantea que cada empresa maneje sus propios datos. Falta confirmar si el sistema será multiempresa. |
| Usuario                  | RF-04, RF-10; CU-02, CU-09                                                  | Sí              | Inicia sesión y queda asociado a las acciones que realiza.                                                            |
| Rol                      | RF-10; CU-09                                                                | Sí              | Indica si el usuario es administrador, gerente o colaborador.                                                         |
| Permiso                  | RF-10; CU-09                                                                | Sí              | Define qué puede consultar o modificar cada rol.                                                                      |
| Producto                 | RF-01, RF-02, RF-03, RF-07, RF-08, RF-11; CU-01, CU-03, CU-04, CU-05, CU-10 | Sí              | Es cada material o elemento registrado en el inventario, con su cantidad y costo.                                     |
| MovimientoInventario     | RF-03, RF-06; CU-03                                                         | Sí              | Guarda las entradas y salidas, la cantidad, la fecha y quién hizo el movimiento.                                      |
| Equipo                   | RF-01, RF-05, RF-12; CU-01, CU-07, CU-11                                    | Sí              | Permite identificar equipos como monitores y torres y consultar dónde están.                                          |
| Ubicacion                | RF-05, RF-12; CU-07, CU-11                                                  | Sí              | Indica dónde está un equipo y permite registrar de dónde salió y a dónde se movió.                                    |
| MovimientoEquipo         | RF-05, RF-06, RF-12; CU-07, CU-11                                           | Sí              | Guarda los cambios de ubicación de un equipo, quién lo movió y cuándo.                                                |
| RegistroAuditoria        | RF-06, RNF-04; CU-07                                                        | Sí              | Deja constancia de quién hizo un cambio y en qué momento.                                                             |
| Tarea                    | RF-13; CU-06                                                                | Sí              | Guarda la tarea asignada por el gerente y el colaborador responsable.                                                 |
| CalculoCosto             | RF-08, RF-09; CU-05, CU-08                                                  | Sí              | Guarda el costo total de un producto o trabajo.                                                                       |
| DetalleCosto             | RF-08, RF-09; CU-05, CU-08                                                  | Sí              | Muestra qué materiales, recursos y otros costos forman el total.                                                      |
| SugerenciaOrganizacionIA | RF-14; CU-12 _(pendiente de confirmar con el cliente)_                      | Sí, provisional | Guarda los datos y el resultado de la sugerencia, si se confirma que se usará esta función.                           |
| Costo unitario           | RF-08; CU-05                                                                | No              | Se puede guardar como un dato del producto; por ahora no requiere una clase propia.                                   |
| Pantalla de inventario   | CU-01, CU-04                                                                | No              | Es parte de la interfaz y no un elemento del dominio.                                                                 |
| …                        |                                                                             |                 |                                                                                                                       |

- **Mínimo 6 clases** que se quedan.
- Toda clase lleva fuente. Una clase que no sale de ningún requisito o caso de uso no está en el alcance.

---

## 3. Diagrama de clases del dominio

Un solo diagrama con:

- **Mínimo 6 clases**, con atributos y tipos.
- **Mínimo 5 relaciones**, cada una con multiplicidad en los dos extremos.
- Al menos **una composición o agregación** y, si el dominio lo justifica, una **herencia**.
- Nombres en el vocabulario del dominio _(el que salió de la elicitación del Taller 3)_.
- Si el proyecto tiene componente de IA, la **entidad que guarda el resultado** del modelo _(e.g. `SugerenciaIA` con fecha, entrada, salida y estado)_. El servicio que llama a la API **no** va en este taller.

**Imagen o enlace al diagrama:** ![Diagrama de clases del punto 3](../Punto%203.png)

---

## 4. Trazabilidad y dudas

**Columna de clase de la matriz**

| Requisito                        | Caso de uso                      | Clase(s)                                                           |
| -------------------------------- | -------------------------------- | ------------------------------------------------------------------ |
| RF-01                            | _(CU-0#)_                        | _(completar)_                                                      |
| …                                |                                  |                                                                    |
| RF-01                            | CU-01                            | Producto, Equipo                                                   |
| RF-02                            | CU-04                            | Producto, MovimientoInventario                                     |
| RF-03                            | CU-03                            | Producto, MovimientoInventario, Usuario                            |
| RF-04                            | CU-02                            | Usuario                                                            |
| RF-05                            | CU-07                            | Equipo, MovimientoEquipo, Ubicacion                                |
| RF-06                            | CU-07                            | Usuario, MovimientoEquipo, MovimientoInventario, RegistroAuditoria |
| RF-07                            | CU-04                            | Producto                                                           |
| RF-08                            | CU-05, CU-08                     | Producto, CalculoCosto, DetalleCosto                               |
| RF-09                            | CU-08                            | CalculoCosto, DetalleCosto, Producto                               |
| RF-10                            | CU-09                            | Usuario, Rol, Permiso                                              |
| RF-11                            | CU-10                            | Producto                                                           |
| RF-12                            | CU-11                            | Equipo, Ubicacion, MovimientoEquipo                                |
| RF-13                            | CU-06                            | Tarea, Usuario                                                     |
| RF-14 _(pendiente de confirmar)_ | CU-12 _(pendiente de confirmar)_ | SugerenciaOrganizacionIA                                           |
| RNF-01                           | CU-03, CU-08                     | Producto, CalculoCosto, DetalleCosto                               |
| RNF-02                           | CU-03, CU-04                     | Usuario, Producto, MovimientoInventario                            |
| RNF-03                           | CU-08, CU-09                     | Usuario, Rol, Permiso                                              |
| RNF-04                           | CU-03, CU-07                     | Usuario, MovimientoInventario, MovimientoEquipo, RegistroAuditoria |
| RNF-05                           | CU-03                            | Producto, MovimientoInventario                                     |

**Aclaración:** En el Taller 4, CU-02 es el inicio de sesión y se agregó RF-04 para cubrirlo. RF-02 corresponde a las cantidades disponibles, así que se relaciona con CU-04.

- Cada caso crítico debe apoyarse en al menos una clase del diagrama.

**Dudas para la siguiente clase** _(lo que el equipo no pudo resolver solo)_:

- _(completar)_
- ¿Cada empresa tendrá sus propios usuarios y productos dentro del sistema, o se usará una instalación distinta para cada empresa?
- ¿Se va a incluir la sugerencia con IA? Si la respuesta es sí, ¿qué información debe usar y qué resultado debe guardar?
- ¿Qué puede hacer cada rol? ¿Un usuario puede tener más de un rol?
- Además de los materiales, ¿qué otros valores se deben incluir al calcular el costo, por ejemplo mano de obra o transporte?
- ¿Cómo se van a identificar los equipos y qué ubicaciones se deben registrar?

---

## Ejemplo diligenciado

**2. Candidatas**

| Clase candidata | Fuente            | ¿Se queda? | Por qué                                                                   |
| --------------- | ----------------- | ---------- | ------------------------------------------------------------------------- |
| Cliente         | RF-01             | Sí         | Reserva y tiene turnos                                                    |
| Turno           | RF-01, CU-01      | Sí         | Concepto central del dominio                                              |
| Barbero         | RF-02             | Sí         | Atiende turnos; tiene agenda                                              |
| Agenda          | P1 _(entrevista)_ | No         | Es la lista de turnos de un barbero en un día: una consulta, no una clase |
| CierreCaja      | RF-05             | Sí         | Guarda el total del día                                                   |
| Teléfono        | RF-01             | No         | Es un atributo de Cliente                                                 |

**3. Diagrama** _(extracto en PlantUML)_

![img01](/docs/diagrams/img-01.png)

**4. Trazabilidad:** RF-01 → CU-01 Reservar turno → Cliente, Turno, Barbero. RF-02 → CU-02 Marcar no asistido → Turno _(estado)_.
