# Ficha de equipo y dominio — Sesión 1

Plantilla de la **actividad de cierre de la Clase 1**. Se diligencia en clase, en equipo, y se entrega al final de la sesión.

- **Equipos:** de 2 a 3 integrantes, fijos durante todo el curso.
- **Entrega:** una ficha por equipo.
- **Cada equipo elige un dominio distinto.**

---

## 1. Identificación del equipo

| Campo | Respuesta |
|---|---|
| Nombre del equipo | _(Gerstock)_ |
| Fecha | _(14-09-2026)_ |

| # | Integrante | Correo | Rol / responsabilidad |
| --- | --- | --- | --- |
| 1 | _(Kevin Rodriguez)_ | _(	kevin.gaviria.0107@miremington.edu.co)_ | Coordinación _(obligatorio)_ |
| 2 | _(David Solarte)_ | _(david.solarte.3418@miremington.edu.co)_ | _(Desarrollador)_ |
| 3 | _(Cristian Martinez)_ | _(cristian.martinez.2555@miremington.edu.co)_ | _(Gestor de cliente)_ |

> El rol no es definitivo: se ajusta en la bitácora de gestión. Lo que sí queda fijo hoy es **quién coordina**.

---

## 2. Dominio propuesto

**Dominio:** _(Gestión de inventarios y costos de producción para empresas.)_

**Problema que se quiere resolver** _(Optimizar los procesos de gestión de inventarios y cálculo de costos de producción de los productos registrados en el sistema.)_:

_(completar)_

**Cómo se hace hoy sin software** _(Actualmente, algunas empresas gestionan sus inventarios y costos mediante Excel y hojas de cálculo, lo que puede generar pérdida de información, errores y procesos que consumen demasiado tiempo. Además, estas herramientas no siempre permiten realizar cálculos de costos de manera eficiente.
)_:

_(completar)_

---

## 3. Usuarios del sistema

| Tipo de usuario | Qué necesita hacer en el sistema | ¿Tenemos acceso para entrevistarlo? |
| --- | --- | --- |
| _(Administrador)_ | _(Permitir el acceso de diferentes usuarios con permisos específicos.)_ | Sí / No — _(quién es)_ |
| _(Gerentes)_ | _(Administrar inventarios y costos de producción.)_ | Sí / No — _(quién es)_ |
| _(Colaboradores)_ | _(Administrar inventario)_ | Sí / No — _(quién es)_ |

> Al menos **un usuario real y accesible** es obligatorio: en la Clase 3 hay que hacerle una sesión de elicitación de verdad.

---

## 4. Capacidad del equipo

**¿Por qué este equipo puede levantar requisitos de este dominio?** _(El sistema tendrá tres roles: el administrador gestionará usuarios y permisos; el gerente administrará el inventario y calculará costos de producción; y el usuario podrá consultar y modificar el inventario.)_

_(completar)_

---

## 5. Alcance tentativo

**Tres cosas que el sistema sí debe hacer**:

1. _(Administrar inventarios)_
2. _(Gestionar costos de producción)_
3. _(Gestionar tarear)_
4. _(Se trabajara de forma local)_

**Tres cosas que el sistema no va a hacer**:

1. _(Modificar precios de proveedor)_
2. _(No manejará nómina ni recursos humanos.)_
3. _(No gestionará pagos ni transacciones bancarias)_

---

## 6. Autoverificación

- [x] Hay **usuarios reales accesibles** para entrevistar en la Clase 3.
- [ ] El dominio da para **10 requisitos funcionales y 5 no funcionales** sin inventarlos.
- [ ] Los **tres casos críticos** se ven implementables end-to-end en seis semanas.
- [x] El proyecto **no fue desarrollado** en otra asignatura ni se está reciclando.
- [x] No es demasiado grande _(una red social completa)_ ni demasiado pequeño _(una calculadora)_.
- [Sí] El sistema **maneja datos personales**: Sí / No. Si es Sí, aplica la Ley 1581 de 2012 en el numeral 10 de la Nota 1.

---

## Ejemplo diligenciado

Referencia de nivel de detalle esperado. **No se puede usar este dominio.**

- **Dominio:** control de turnos en una barbería de barrio con tres sillas.
- **Problema:** los turnos se anotan en un cuaderno; los clientes llegan sin saber la espera y se van, y el dueño no sabe cuánto factura cada barbero al mes.
- **Hoy:** cuaderno físico y llamadas telefónicas.
- **Usuarios:** cliente _(reserva y consulta su turno)_, barbero _(ve su agenda del día)_, administrador _(cierra caja y ve el reporte mensual)_. Acceso real: el tío de un integrante es dueño del local.
- **Sí hace:** reservar turno, ver agenda del día por barbero, cerrar caja con reporte de ingresos.
- **No hace:** pagos en línea, domicilios, inventario de productos.

---

## Flujo del Proyecto

```bash
UI → Controlador → ServicioIA «interfaz» → AdaptadorProveedor → API del modelo → AdaptadorSimulado → respuesta fija (pruebas)
```