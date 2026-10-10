# Taller 4 · Casos de uso

Se trabaja en clase, por equipo.

- **Entrega:** en el **repositorio del equipo en GitHub**, diligenciando el enunciado con los puntos 1 a 5 y subiendo el diagrama al repositorio _(imagen exportada o fuente PlantUML/draw.io)_.
- Herramienta: draw.io, PlantUML, StarUML o Visual Paradigm.

---

## 1. Actores y casos

**Actores**

| Actor                  | Tipo _(humano / sistema externo / tiempo)_ | Principal o secundario | Objetivo en el sistema                                                  |
| ---------------------- | ------------------------------------------ | ---------------------- | ----------------------------------------------------------------------- |
| _(ADMINISTRADOR)_      | _(Humano)_                                 | _(Principal)_          | _(administrar y supervisar el correcto funcionamiento del sistema)_     |
| _(GERENTE)_            | _(Humano)_                                 | _(Principal)_          | _(administrar y organizar el inventario y tareas asignadas)_            |
| _(COLABORADOR)_        | _(Humano)_                                 | _(Principal)_          | _(organiza y documenta los movimientos relacionados con el inventario)_ |
| _(IA DE ORGANIZACION)_ | _(Sistema externo)_                        | _(Secundario)_         | _(apoya en los procesos de organizacion de materias prímas)_            |
| …                      |                                            |                        |                                                                         |

- Roles, no personas. La base de datos y el servidor **no** son actores.
- Si el proyecto tiene componente de IA, el **proveedor del modelo** es un actor secundario.

**Casos de uso**

| ID    | Nombre _(verbo en infinitivo + objeto)_                        | Actor principal                    | RF que cubre     |
| ----- | -------------------------------------------------------------- | ---------------------------------- | ---------------- |
| CU-01 | _(registrar los productos o elementos del inventario)_         | _(COLABORADOR)_                    | _(RF-01)_        |
| CU-02 | _(Iniciar sesión dentro del sistema)_                          | _(COLABORADOR,ADMINISTRADOR y ge)_ | _(RF-02)_        |
| CU-03 | _(Controlar entradas y salidas de materiales )_                | _(COLABORADOR Y ADMINISTRADOR)_    | _(RF-03)_        |
| CU-04 | _(Consultar la cantidad de material disponible)_               | _(COLABORADOR Y ADMINISTRADOR)_    | _(RF-07)_        |
| CU-05 | _(Consultar los costos asociados con los materiales)_          | _(ADMINISTRADOR)_                  | _(RF-08)_        |
| CU-06 | _(Asignar tareas a los colaboradores)_                         | _(GERENTE)_                        | _(RF-13)_        |
| CU-07 | _(Registrar el movimiento de un equipo o elemento)_            | _(COLABORADOR)_                    | _(RF-05, RF-06)_ |
| CU-08 | _(Calcular el costo de producción de un producto o trabajo)_   | _(GERENTE)_                        | _(RF-09)_        |
| CU-09 | _(Administrar usuarios y permisos por rol)_                    | _(ADMINISTRADOR)_                  | _(RF-10)_        |
| CU-10 | _(Modificar o eliminar productos o elementos registrados)_     | _(GERENTE)_                        | _(RF-11)_        |
| CU-11 | _(Consultar la existencia y ubicación de equipos o elementos)_ | _(COLABORADOR)_                    | _(RF-12)_        |
| CU-12 | _(Sugerir la organización de materias primas con IA)_          | _(GERENTE)_                        | _(RF-14)_        |
| …     |                                                                |                                    |                  |

- **Mínimo 6 casos**, todos con al menos un RF.

---

## 2. Diagrama de casos de uso

Un solo diagrama con:

- **Límite del sistema** con su nombre; los casos dentro, los actores fuera.
- Todos los casos del punto 1 y sus asociaciones con los actores.
- Al menos una relación **`«include»`, `«extend»` o generalización**, justificada en una línea. Si el dominio no pide ninguna, se escribe por qué.

**Imagen o enlace al diagrama:** ![Diagrama de casos de uso](../Diagrama_gestion_inventario.png)

**Justificación de las relaciones:**

- **CU-03 `«include»` CU-04:** toda salida de material debe verificar primero la cantidad disponible, para evitar que dos trabajadores soliciten el mismo elemento cuando solo hay una unidad _(P7)_; además, la consulta de cantidades también se usa sola _(P5)_.
- **CU-08 `«include»` CU-05:** el cálculo del costo de producción siempre parte de los costos de los materiales registrados _(P4, P5)_, y esos costos también se consultan sin calcular nada.
- **GERENTE hereda de COLABORADOR (generalización):** el gerente puede hacer todo lo que hace un colaborador sobre el inventario, además de asignar tareas y calcular costos.

---

## 3. Casos críticos

Los tres casos que el prototipo implementa **de punta a punta** _(de la interfaz a la persistencia)_.

| Caso      | Por qué es crítico _(valor / frecuencia / riesgo técnico)_                                                                                                                                                                                                                                          |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _(CU-03)_ | _(Valor: es el núcleo del inventario, pues mantiene actualizada la cantidad real de materiales. Frecuencia: se usa cada vez que un material entra o sale. Riesgo técnico: concurrencia, ya que dos trabajadores pueden pedir el mismo elemento cuando solo hay una unidad (P7, RNF-05).)_           |
| _(CU-07)_ | _(Valor: resuelve el dolor principal, que los equipos se mueven sin actualizar el registro y el inventario no coincide con la realidad (P3, P6). Frecuencia: cada movimiento de equipos entre puestos. Riesgo: sin trazabilidad de quién y cuándo, la empresa puede enfrentar sanciones (RNF-04).)_ |
| _(CU-08)_ | _(Valor: reemplaza el cálculo manual en hojas de cálculo, propenso a errores (P4). Frecuencia: cada trabajo o producto cotizado o fabricado. Riesgo técnico: la fórmula combina materiales, recursos y otros costos, y un error de cálculo afecta directamente el dinero de la empresa.)_           |

- **Máximo uno** puede ser el caso de IA; los otros dos son funcionalidad con persistencia propia.
- No valen iniciar sesión.

---

## 4. Descripción detallada de los casos críticos

Una tabla por caso crítico.

### CU-03 Controlar entradas y salidas de materiales

| Campo                    | Contenido                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------- |
| **ID y nombre**          | CU-03 Controlar entradas y salidas de materiales                                                         |
| **Actor principal**      | Colaborador _(también lo realiza el Administrador)_                                                      |
| **Actores secundarios**  | —                                                                                                        |
| **Requisitos que cubre** | RF-03, RF-07, RNF-01, RNF-04, RNF-05                                                                     |
| **Precondiciones**       | El usuario inició sesión y el material ya está registrado en el inventario                               |
| **Disparador**           | Un material ingresa a la empresa o un trabajador solicita un material para usarlo                        |
| **Frecuencia**           | Varias veces al día _(P2, P8; la cifra exacta queda pendiente de confirmar con el cliente del proyecto)_ |

**Flujo principal**

1. El colaborador indica que va a registrar un movimiento de material.
2. El sistema solicita el tipo de movimiento (entrada o salida).
3. El colaborador elige el material y la cantidad.
4. El sistema verifica la cantidad disponible del material (incluye CU-04).
5. El sistema valida que la cantidad sea válida y, en una salida, que no supere la disponible.
6. El colaborador indica a quién se entrega el material (en una salida) o su procedencia (en una entrada).
7. El colaborador confirma el movimiento.
8. El sistema actualiza la cantidad disponible y guarda el movimiento con usuario, fecha y hora.
9. El sistema informa que el movimiento quedó registrado.

**Flujos alternos** _(se logra el objetivo por otro camino)_

- **5a.** La cantidad solicitada es mayor que la disponible: el sistema informa la existencia real y permite al colaborador ajustar la cantidad. Vuelve al paso 3.
- **8a.** El material queda por debajo del nivel mínimo de existencias: el sistema registra el movimiento y además avisa que conviene reponerlo. Continúa en el paso 9.

**Excepciones** _(no se logra el objetivo)_

- **8b.** Otro usuario tomó la última unidad en el mismo momento _(concurrencia)_: el sistema rechaza el movimiento, informa que la existencia cambió y no modifica el inventario. El caso termina sin registro.
- **8c.** Falla al guardar en la base de datos: el sistema informa el error, no modifica cantidades y registra el evento. El caso termina sin registro.

**Postcondiciones**

- **Éxito:** la cantidad del material refleja la entrada o salida, y queda registrado quién hizo el movimiento, cuándo y a quién se entregó.
- **Garantía mínima:** nunca queda un movimiento a medias ni una cantidad negativa; ante cualquier falla el inventario permanece como estaba.

---

### CU-07 Registrar el movimiento de un equipo o elemento

| Campo                    | Contenido                                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **ID y nombre**          | CU-07 Registrar el movimiento de un equipo o elemento                                                                     |
| **Actor principal**      | Colaborador                                                                                                               |
| **Actores secundarios**  | —                                                                                                                         |
| **Requisitos que cubre** | RF-05, RF-06, RF-12, RNF-04                                                                                               |
| **Precondiciones**       | El usuario inició sesión y el equipo o elemento está registrado con su ubicación actual                                   |
| **Disparador**           | Un trabajador traslada o intercambia un equipo (monitor, torre u otro) de un puesto a otro                                |
| **Frecuencia**           | Cada vez que se mueve un equipo; hoy se informa por correo al coordinador _(P2, P6; cifra exacta pendiente de confirmar)_ |

**Flujo principal**

1. El colaborador indica que va a registrar el movimiento de un equipo.
2. El sistema solicita identificar el equipo.
3. El colaborador identifica el equipo.
4. El sistema muestra la ubicación y el responsable actuales del equipo.
5. El colaborador indica la nueva ubicación y, si aplica, el nuevo responsable.
6. El sistema valida que los datos estén completos y que la nueva ubicación sea distinta de la actual.
7. El colaborador confirma el movimiento.
8. El sistema actualiza la ubicación del equipo y guarda el movimiento con usuario, fecha y hora.
9. El sistema informa que el movimiento quedó registrado.

**Flujos alternos** _(se logra el objetivo por otro camino)_

- **3a.** El equipo no está registrado: el sistema ofrece registrarlo primero (CU-01) y luego continúa. Vuelve al paso 3.
- **6a.** Faltan datos obligatorios: el sistema indica cuáles faltan y permite completarlos. Vuelve al paso 5.

**Excepciones** _(no se logra el objetivo)_

- **6b.** El equipo fue movido por otra persona y su ubicación cambió desde que se consultó: el sistema informa la ubicación actualizada y no guarda el movimiento. El caso termina sin registro.
- **8a.** Falla al guardar en la base de datos: el sistema informa el error, conserva la ubicación anterior y registra el evento. El caso termina sin registro.

**Postcondiciones**

- **Éxito:** la ubicación registrada del equipo coincide con la real y queda el historial de quién lo movió, cuándo y desde dónde.
- **Garantía mínima:** la ubicación anterior del equipo nunca se pierde ni queda en un estado inconsistente.

---

### CU-08 Calcular el costo de producción de un producto o trabajo

| Campo                    | Contenido                                                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **ID y nombre**          | CU-08 Calcular el costo de producción de un producto o trabajo                                                       |
| **Actor principal**      | Gerente                                                                                                              |
| **Actores secundarios**  | Asistente IA                                                                                                         |
| **Requisitos que cubre** | RF-09, RF-08, RNF-01, RNF-03                                                                                         |
| **Precondiciones**       | El gerente inició sesión y los materiales tienen costo registrado                                                    |
| **Disparador**           | El gerente necesita conocer cuánto cuesta fabricar un producto o realizar un trabajo (por ejemplo, instalar una red) |
| **Frecuencia**           | Cada vez que se cotiza o se produce un trabajo _(P4; frecuencia exacta pendiente de confirmar)_                      |

**Flujo principal**

1. El gerente indica que va a calcular el costo de un producto o trabajo.
2. El sistema solicita el nombre del producto o trabajo.
3. El gerente indica los materiales y las cantidades utilizadas.
4. El sistema consulta el costo de cada material (incluye CU-05).
5. El gerente indica los recursos y otros costos asociados al trabajo.
6. El sistema valida que las cantidades y los valores sean numéricos y positivos.
7. El sistema calcula el costo de cada componente y el costo total.
8. El sistema presenta el desglose y el costo total.
9. El gerente confirma y el sistema guarda el cálculo.

**Flujos alternos** _(se logra el objetivo por otro camino)_

- **3a.** El producto ya tiene un cálculo guardado: el sistema lo carga como base y el gerente lo ajusta. Vuelve al paso 3.
- **8a.** El gerente quiere cambiar un dato tras ver el resultado: el sistema permite corregirlo y recalcula. Vuelve al paso 3.

**Excepciones** _(no se logra el objetivo)_

- **4a.** Un material no tiene costo registrado: el sistema indica cuál es, no calcula el total y sugiere registrar el costo. El caso termina sin cálculo.
- **9a.** Falla al guardar en la base de datos: el sistema presenta el resultado sin guardarlo, informa el error y registra el evento. El caso termina sin cálculo guardado.

**Postcondiciones**

- **Éxito:** queda guardado el costo total del producto o trabajo con su desglose de materiales, recursos y otros costos.
- **Garantía mínima:** nunca se guarda un cálculo incompleto ni con valores inválidos, y los costos de los materiales no cambian.

- **Mínimo por caso:** 5 pasos en el flujo principal, **un flujo alterno y una excepción**.
- Pasos con un sujeto _(el actor o el sistema)_ y sin detalles de interfaz: _"elige la franja"_, no _"hace clic en el botón"_.
- Si uno de los críticos es el de IA, sus excepciones incluyen **timeout, cuota agotada y respuesta malformada**.

---

## 5. Trazabilidad

**Columna de caso de uso de la matriz** _(la que se abrió en la Clase 3)_:

| Requisito       | Fuente                                                                 | Caso de uso  |
| --------------- | ---------------------------------------------------------------------- | ------------ |
| RF-01           | P2                                                                     | CU-01        |
| RF-02           | P5                                                                     | CU-02, CU-04 |
| RF-03           | P2                                                                     | CU-03        |
| RF-04 _(nuevo)_ | P10                                                                    | CU-02        |
| RF-05           | P6                                                                     | CU-07        |
| RF-06           | P3                                                                     | CU-07        |
| RF-07           | P5                                                                     | CU-04        |
| RF-08           | P5                                                                     | CU-05        |
| RF-09           | P4                                                                     | CU-08        |
| RF-10           | P10                                                                    | CU-09        |
| RF-11           | P2                                                                     | CU-10        |
| RF-12           | P6                                                                     | CU-11        |
| RF-13 _(nuevo)_ | P1                                                                     | CU-06        |
| RF-14 _(nuevo)_ | Alcance de la ficha (IA de organización); por confirmar con el cliente | CU-12        |
| …               |                                                                        |              |

**Huecos detectados:**

| Hueco              | Cuál                                                                                                                                 | Qué se hace                                                                                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RF sin caso de uso | RF-10, RF-11 y RF-12 no tenían caso de uso. Además, RF-04 no existe en el catálogo del Taller 3 (salto de numeración).               | Se crean CU-09 (RF-10), CU-10 (RF-11) y CU-11 (RF-12). Se crea RF-04 "El sistema debe permitir iniciar sesión según el rol" para CU-02.                                                                                               |
| Caso de uso sin RF | CU-06 Asignar tareas, CU-12 Sugerir organización con IA y CU-02 Iniciar sesión (cita RF-02, que en el Taller 3 trata de cantidades). | Se agregan RF-13 (asignar tareas a personas específicas, P1), RF-14 (sugerir organización de materias primas con IA, por confirmar con el cliente) y RF-04 (iniciar sesión). Si el cliente no confirma RF-14, CU-12 sale del alcance. |

- Todo lo que cambie el catálogo va al **registro de control de cambios** de la bitácora: alta de RF-04, RF-13 y RF-14, y la confirmación pendiente de CU-12.

---

## Ejemplo diligenciado

Referencia de nivel de detalle. Mismo dominio de los talleres anteriores: **no se puede usar.**

**1. Actores** _(barbería; extracto)_

| Actor           | Tipo                         | Principal o secundario | Objetivo                                         |
| --------------- | ---------------------------- | ---------------------- | ------------------------------------------------ |
| Cliente         | Humano                       | Principal              | Conseguir un turno sin llamar                    |
| Barbero         | Humano                       | Principal              | Saber a quién atiende y registrar quién no llegó |
| Dueño           | Humano _(hereda de Barbero)_ | Principal              | Cerrar caja y mantener la clientela              |
| Proveedor de IA | Sistema externo              | Secundario             | Redactar el texto del recordatorio               |

**1. Casos** _(extracto)_

| ID    | Nombre                       | Actor principal | RF    |
| ----- | ---------------------------- | --------------- | ----- |
| CU-01 | Reservar turno               | Cliente         | RF-01 |
| CU-02 | Consultar franjas libres     | Cliente         | RF-01 |
| CU-03 | Cancelar turno               | Cliente         | RF-04 |
| CU-05 | Marcar turno no asistido     | Barbero         | RF-02 |
| CU-06 | Cerrar caja del día          | Dueño           | RF-05 |
| CU-07 | Redactar recordatorio con IA | Dueño           | RF-08 |

**2. Relaciones:** CU-01 `«include»` CU-02, porque toda reserva pasa por consultar las franjas y el cliente también las consulta sin reservar. Dueño hereda de Barbero, porque el dueño también atiende una silla.

**3. Críticos**

| Caso                               | Por qué                                                                                                                |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| CU-01 Reservar turno               | Es el problema que se tiene es: el teléfono no para los sábados; ~40 al día; riesgo de dos reservas en la misma franja |
| CU-06 Cerrar caja del día          | Todos los días; cálculo sobre los turnos atendidos                                                                     |
| CU-07 Redactar recordatorio con IA | El caso de IA; reduce los no asistidos _(P6)_                                                                          |

**4. Descripción** _(CU-07; CU-01 está completo en la Sesión 5)_

| Campo                   | Contenido                                            |
| ----------------------- | ---------------------------------------------------- |
| **Actor principal**     | Dueño                                                |
| **Actores secundarios** | Proveedor de IA                                      |
| **Requisitos**          | RF-08, RNF-04 _(respuesta en menos de 10 s)_         |
| **Precondiciones**      | Hay turnos _Reservados_ para el día siguiente        |
| **Disparador**          | El dueño prepara los recordatorios al cierre del día |
| **Frecuencia**          | Una vez al día                                       |

1. El dueño pide los recordatorios del día siguiente.
2. El sistema lista los turnos _Reservados_ de mañana.
3. El sistema envía al proveedor de IA la franja, el barbero y el nombre de pila de cada cliente, **sin teléfono**.
4. El proveedor devuelve un borrador de mensaje por turno.
5. El sistema valida que cada borrador traiga fecha y franja, y los muestra marcados como _texto generado_.
6. El dueño revisa, edita si quiere y aprueba.
7. El sistema guarda los mensajes aprobados listos para enviar.

- **5a.** Un borrador no trae fecha o franja: se descarta y se usa la plantilla fija para ese turno. Vuelve al paso 6.
- **6a.** El dueño descarta un borrador: el sistema usa la plantilla fija para ese turno. Vuelve al paso 6.
- **4a.** _(excepción)_ El proveedor no responde en 10 s o devuelve HTTP 429: el sistema informa que la IA no está disponible, registra el evento y ofrece la plantilla fija para todos. El caso termina sin texto generado.

**Postcondiciones.** Éxito: cada turno de mañana tiene un mensaje aprobado. Garantía mínima: ningún dato de contacto sale hacia el proveedor.

**5. Huecos:** RF-06 _(reporte mensual de ingresos)_ sin caso → se crea CU-09 Consultar reporte mensual. CU-04 Avisar a la lista de espera sin RF → se agrega RF-11 y se registra en el control de cambios.
