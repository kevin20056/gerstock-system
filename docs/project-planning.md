# Taller  2· Metodología y tablero

Enunciado del **Taller 2**. Se trabaja en clase, en equipo, y se entrega al final de la sesión.

- **Entrega:** un documento por equipo con los puntos 1, 2, 3 y 5, más el **enlace al tablero** del punto 4 con el docente invitado.
- **Nota:** cuenta dentro de los Talleres 1 a 6 *(60% del Seguimiento)*. **No es recuperable**: se califica con la asistencia y el trabajo hecho en la sesión.
- **Requisito previo:** ficha de dominio aprobada en el primer taller. Si quedó con ajustes, se resuelven en los primeros 5 minutos.
- Lo que se produce aquí se reutiliza: la justificación pasa al **numeral 5** de la Nota 1 y el tablero con su acta abren la **bitácora de gestión**.

---

## 1. Caracterización del dominio

Ubicar el proyecto en cada factor **con un dato concreto del dominio**, no con una opinión. Una celda que dice "medio" sin evidencia no cuenta.

| Factor | Valoración *(ágil ← → plan)* | Evidencia del dominio |
| --- | --- | --- |
| Tamaño | *(Agil)* | *(Equipo de tres integrantes y programa pequeño)* |
| Criticidad | *(Plan)* | *(Un fallo cuesta dinero y recursos)* |
| Dinamismo de los requisitos | *(Plan)* | *(Requisitos optimos para un funcionamiento correcto)* |
| Personal *(experiencia del equipo)* | *(Agil)* | *(Equipo con experiencia media)* |
| Cultura *(del cliente u organización)* | *(Plan)* | *(Flexibilidad a las decisiones del cliente)* |
| Acceso al cliente | *(Agil)* | *(Sistema de interfaz compacta y facil de usar)* |
| Regulación | *(Plan)* | *(Constante asesoria con el funcionamiento del sistema)* |

---

## 2. Selección y justificación

**Metodología elegida:** *(Kanban)*

**Justificación** *(un párrafo que cite al menos tres factores del punto 1)*:Se seleccionó la metodología Kanban debido a que su enfoque ágil facilita un monitoreo dinámico y continuo de cada tarea. Esto nos permite adaptarnos rápidamente a los requerimientos del sistema, optimizar tiempos de entrega y mantener un control claro sobre el progreso del desarrollo.

*(completar)*

**Alternativas descartadas** *(mínimo dos)*:

| Alternativa | Por qué no encaja en este dominio |
| --- | --- |
| *(Cascada)* | *(Por su poca flexibilidad ante los cambios)* |
| *(Espiral)* | *(Cascada es muy rígida: como todo se entrega al final, cualquier cambio obliga a desechar lo hecho y rehacer el trabajo.)* |

> "Porque es la más usada" o "porque es flexible" no son justificaciones: no dicen nada del dominio.

---

## 3. Adaptación

Explicar cómo se organiza el equipo **dentro** de ellas.

| Campo | Respuesta |
| --- | --- |
| 2 Semanas | *(Se va estipular de dos semanas)* |
| Reuniones | *(Cada 2 días)* |
| Intermedio | *(Cumplir mas de la mitad un 60%)* |

**Roles asignados** *(ajustar los nombres a la metodología elegida)*:

| Integrante | Rol | Qué hace en la práctica |
| --- | --- | --- |
| *(Cristian Martinez)* | *(e.g. Product Owner)* | *(Define qué hacer requerimientos y prioridades)* |
| *(Kevin Rodriguez)* | *(e.g. Scrum Master)* | *(Coordina el flujo y elimina bloqueos)* |
| *(David Solarte)* | *(e.g. developer)* | *(Diseña, programa y prueba el software)* |

**Definición de Hecho** *(mínimo tres condiciones verificables para que una tarjeta pase a Hecho)*:

1. *(Procceso)*
2. *(Revisión)*
3. *(completado)*

---

## 4. Tablero y backlog inicial

Crear el tablero en **GitHub Projects**, Trello o Jira e **invitar al docente**.

**Mínimos del tablero:**

- Columnas: *Backlog · Por hacer · En progreso · En revisión · Hecho* *(o equivalentes, justificadas)*.
- **Límite de WIP** declarado en *En progreso*.
- **Mínimo 10 tarjetas** con el trabajo hasta la Nota 1 *(Clase 4)*. Los requisitos del producto todavía no existen: el backlog de hoy es de **tareas del proyecto** *(preparar la entrevista, redactar el problema, catalogar RF y RNF, armar la sustentación…)*.
- Cada tarjeta con **responsable, estimación** *(horas o puntos)* y **fecha límite**.
- **Todos los integrantes** con al menos una tarjeta asignada.

**Enlace al tablero:** *(completar)*

**Método de estimación usado:** *(horas)*

---

## 5. Primera acta

Primera entrada de la bitácora de gestión.

| Campo | Respuesta |
| --- | --- |
| Fecha | *(completar)* |
| Asistentes | *(completar)* |
| Decisiones tomadas | *(completar)* |
| Compromisos *(quién, qué)* | *(completar)* |
| Bloqueos o riesgos | *(completar)* |

## Ejemplo diligenciado

Referencia de nivel de detalle. Mismo dominio del ejemplo de la ficha: **no se puede usar.**

**1. Caracterización** *(barbería de barrio con tres sillas)*

| Factor | Valoración | Evidencia |
| --- | --- | --- |
| Tamaño | Ágil | Equipo de 3; un solo interesado con poder de decisión *(el dueño)* |
| Criticidad | Ágil | Si el sistema falla se vuelve al cuaderno; no hay riesgo físico ni pérdida grave |
| Dinamismo | Ágil | El dueño no sabe si quiere reservas por WhatsApp o por web hasta ver una pantalla |
| Personal | Intermedio | Nadie ha trabajado con Scrum; dos integrantes han hecho proyectos web |
| Cultura | Ágil | El dueño acepta ver avances parciales y opinar |
| Acceso al cliente | Ágil | El tío de un integrante; disponible los lunes |
| Regulación | Plan *(leve)* | Maneja nombres y teléfonos: Ley 1581 de 2012, sin norma sectorial |

**2. Selección:** Scrum. Los requisitos van a cambiar cuando el dueño vea las primeras pantallas *(dinamismo)*, un fallo es recuperable *(criticidad)* y hay acceso semanal al dueño para las Review *(acceso al cliente)*. Descartamos **cascada** porque obliga a cerrar requisitos que el dueño aún no conoce, y **Kanban** porque el trabajo sí se puede planificar en bloques y necesitamos un compromiso semanal ligado a las fechas de entrega.

**3. Adaptación:** Sprint de dos semanas. Planning el lunes por videollamada, Review con el dueño el lunes siguiente, Retro al final de la segunda clase de la semana. Daily por chat del equipo, tres preguntas por escrito. DoD: revisado por otro integrante, subido al repositorio, enlazado en la tarjeta.

**4. Tablero:** GitHub Projects, WIP de 3 en *En progreso*. 12 tarjetas estimadas en horas, entre ellas *Preparar guion de entrevista (2 h)*, *Entrevistar al dueño (1 h)*, *Redactar problema y alcance (3 h)*, *Catalogar RF (4 h)*, *Ensayar sustentación (2 h)*.

**5. Acta:** se decide Scrum con Sprint semanal; compromiso de agendar la entrevista con el dueño antes de la primera entrega.
