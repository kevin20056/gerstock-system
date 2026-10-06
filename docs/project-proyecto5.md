# Taller 5 · Diagrama de clases

- **Entrega:** en el **repositorio del equipo en GitHub**, diligenciando el enunciado con los puntos 2, 3 y 4 y subiendo el diagrama al repositorio *(imagen exportada o fuente PlantUML/draw.io)*.
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

| Notación | Significa |
| --- | --- |
| `1` | exactamente uno |
| `0..1` | cero o uno |
| `*` o `0..*` | cero o muchos |
| `1..*` | uno o muchos |

- `Cliente 1 —— 0..* Turno`: un cliente tiene cero o muchos turnos; cada turno es de exactamente un cliente.
- Una relación sin multiplicidad está incompleta.

### Navegabilidad

- Flecha abierta en un extremo: desde A se llega a B, pero no al revés.
- En el modelo de dominio se puede dejar sin flecha *(bidireccional)*; se decide en el diseño.

### Cómo encontrar las clases

1. Subrayar los **sustantivos** del catálogo de requisitos y de las descripciones de los casos de uso.
2. Descartar sinónimos, atributos disfrazados *(el "nombre" no es una clase)*, actores que no guardan datos y cosas fuera del alcance.
3. Lo que queda son **clases candidatas**. Los **verbos** entre ellas sugieren relaciones.

---

## 2. Clases candidatas

| Clase candidata | Fuente *(RF o caso de uso)* | ¿Se queda? | Por qué |
| --- | --- | --- | --- |
| *(completar)* | *(RF-0#, CU-0#)* | Sí / No | *(completar)* |
| … | | | |

- **Mínimo 6 clases** que se quedan.
- Toda clase lleva fuente. Una clase que no sale de ningún requisito o caso de uso no está en el alcance.

---

## 3. Diagrama de clases del dominio

Un solo diagrama con:

- **Mínimo 6 clases**, con atributos y tipos.
- **Mínimo 5 relaciones**, cada una con multiplicidad en los dos extremos.
- Al menos **una composición o agregación** y, si el dominio lo justifica, una **herencia**.
- Nombres en el vocabulario del dominio *(el que salió de la elicitación del Taller 3)*.
- Si el proyecto tiene componente de IA, la **entidad que guarda el resultado** del modelo *(e.g. `SugerenciaIA` con fecha, entrada, salida y estado)*. El servicio que llama a la API **no** va en este taller.

**Imagen o enlace al diagrama:** *(completar)*

---

## 4. Trazabilidad y dudas

**Columna de clase de la matriz**

| Requisito | Caso de uso | Clase(s)      |
| --------- | ----------- | ------------- |
| RF-01     | *(CU-0#)*   | *(completar)* |
| …         |             |               |

- Cada caso crítico debe apoyarse en al menos una clase del diagrama.

**Dudas para la siguiente clase** *(lo que el equipo no pudo resolver solo)*:

- *(completar)*

---

## Ejemplo diligenciado

**2. Candidatas**

| Clase candidata | Fuente            | ¿Se queda? | Por qué                                                                   |
| --------------- | ----------------- | ---------- | ------------------------------------------------------------------------- |
| Cliente         | RF-01             | Sí         | Reserva y tiene turnos                                                    |
| Turno           | RF-01, CU-01      | Sí         | Concepto central del dominio                                              |
| Barbero         | RF-02             | Sí         | Atiende turnos; tiene agenda                                              |
| Agenda          | P1 *(entrevista)* | No         | Es la lista de turnos de un barbero en un día: una consulta, no una clase |
| CierreCaja      | RF-05             | Sí         | Guarda el total del día                                                   |
| Teléfono        | RF-01             | No         | Es un atributo de Cliente                                                 |

**3. Diagrama** *(extracto en PlantUML)*

![img01](/docs/diagrams/img-01.png)

**4. Trazabilidad:** RF-01 → CU-01 Reservar turno → Cliente, Turno, Barbero. RF-02 → CU-02 Marcar no asistido → Turno *(estado)*.