# HACKATHON COPA 2026 — SIMULACRO CTF LOCAL
## API • HTTP • Troubleshooting • Observabilidad

**Duración recomendada:** 60–90 minutos  
**Modalidad:** equipo de 4 personas  
**Infraestructura:** local, sin Azure  
**Objetivo principal:** identificar, demostrar y corregir fallos con la mayor velocidad posible.

---

## ESCENARIO

El equipo recibe una API interna llamada **Copa Incident Service**.

El servicio fue entregado por otro equipo y actualmente presenta varios comportamientos incorrectos. La aplicación inicia, pero no cumple completamente con el contrato solicitado.

Cada integrante debe tomar **UN reto interno**.

Los cuatro retos forman parte del MISMO proyecto.

### Integrante 1
Reto 1 — Contrato REST + códigos HTTP

### Integrante 2
Reto 2 — Headers, autenticación y validación

### Integrante 3
Reto 3 — Health checks y dependencia local

### Integrante 4
Reto 4 — Logs, HTTP 500 y CORS

Cuando cada integrante termine, el equipo debe integrar los cambios y ejecutar la validación final.

---

# REGLAS GENERALES

1. No cambiar nombres de endpoints.
2. No eliminar validaciones para “hacer que funcione”.
3. No devolver HTTP 200 para ocultar errores.
4. No eliminar health checks.
5. No hardcodear secretos nuevos.
6. No sustituir la aplicación completa por otra.
7. Cada integrante debe dejar evidencia de cómo identificó el problema.
8. Cada cambio debe poder justificarse.
9. La prioridad es velocidad + evidencia + corrección mínima.
10. Se permite usar:
   - curl
   - Postman
   - Swagger `/docs`
   - logs de terminal
   - Python
   - Git/GitHub
   - navegador
   - PowerShell

---

# RETO 1 — CONTRATO REST + HTTP
**Responsable sugerido:** Integrante 1

La API de incidencias debe cumplir el siguiente contrato.

## Endpoints

### POST `/api/incidents`
Debe crear una incidencia.

Entrada de ejemplo:

```json
{
  "title": "VPN no disponible",
  "description": "El usuario no puede conectarse",
  "priority": "high"
}
```

Comportamiento esperado:
- Creación correcta → HTTP **201**

---

### GET `/api/incidents`
Debe listar las incidencias.

Comportamiento esperado:
- Solicitud correcta → HTTP **200**

---

### GET `/api/incidents/{id}`
Comportamiento esperado:
- Incidencia existente → HTTP **200**
- Incidencia inexistente → HTTP **404**

---

### PATCH `/api/incidents/{id}`
Debe permitir modificación parcial.

Comportamiento esperado:
- Incidencia existente → HTTP **200**
- Incidencia inexistente → HTTP **404**

---

### DELETE `/api/incidents/{id}`
Comportamiento esperado:
- Eliminación correcta → HTTP **204**
- Incidencia inexistente → HTTP **404**

## Entregable del integrante 1
- Evidencia del comportamiento incorrecto.
- Causa raíz.
- Cambio mínimo.
- Evidencia de los códigos HTTP finales.

---

# RETO 2 — HEADERS, AUTENTICACIÓN Y VALIDACIÓN
**Responsable sugerido:** Integrante 2

Existe un endpoint privado:

### GET `/api/private/summary`

Debe utilizar el header:

```text
X-API-Key
```

La clave válida se obtiene desde la variable:

```text
LAB_API_KEY
```

Comportamiento esperado:

- Header ausente → HTTP **401**
- Clave incorrecta → HTTP **403**
- Clave correcta → HTTP **200**

La respuesta válida debe tener una estructura similar a:

```json
{
  "service": "private-summary",
  "status": "authorized",
  "incidents_total": 0
}
```

No se permite devolver la API key en la respuesta.

---

También existe:

### POST `/api/private/echo`

Entrada válida:

```json
{
  "message": "hola"
}
```

El campo `message` es obligatorio.

Una solicitud que no cumpla el esquema debe generar el error de validación HTTP correspondiente.

## Entregable del integrante 2
- Pruebas con header ausente, incorrecto y correcto.
- Evidencia de validación JSON.
- Causa raíz de cualquier comportamiento incorrecto encontrado.
- Cambio mínimo.

---

# RETO 3 — HEALTH CHECKS Y DEPENDENCIA
**Responsable sugerido:** Integrante 3

La aplicación expone:

### GET `/health/live`

Pregunta que debe responder:

> ¿El proceso de la API está vivo?

Si FastAPI está funcionando debe responder:

```text
HTTP 200
```

---

### GET `/health/ready`

Pregunta que debe responder:

> ¿La aplicación está lista para trabajar con su dependencia de datos?

La aplicación utiliza una base SQLite local incluida en el proyecto.

Comportamiento esperado:

Cuando la dependencia funciona:

```json
{
  "app": "healthy",
  "database": "healthy"
}
```

HTTP **200**

Si la dependencia falla:

```json
{
  "app": "healthy",
  "database": "unhealthy"
}
```

HTTP **503**

## Condición importante

Una dependencia caída NO debe hacer que `/health/live` falle.

## Entregable del integrante 3
- Estado inicial de `/live`.
- Estado inicial de `/ready`.
- Evidencia de la dependencia local.
- Diagnóstico.
- Cambio mínimo.
- Validación final.

---

# RETO 4 — LOGS + HTTP 500 + CORS
**Responsable sugerido:** Integrante 4

La API genera logs de requests en la terminal.

Existe:

### GET `/api/reports/{report_id}`

La mayoría de IDs funcionan, pero existe al menos un caso que genera:

```text
HTTP 500
```

El objetivo es:

1. reproducir el fallo;
2. identificar el request exacto;
3. usar logs/traceback como evidencia;
4. encontrar la causa raíz;
5. aplicar el cambio mínimo;
6. demostrar que el endpoint dejó de generar 500.

No se permite eliminar el endpoint ni capturar todas las excepciones devolviendo HTTP 200.

---

## CORS

La aplicación debe aceptar requests desde:

```text
http://localhost:3000
```

El equipo debe validar la configuración CORS.

Puede investigarse con navegador, Postman o una petición OPTIONS/curl que incluya un `Origin`.

## Entregable del integrante 4
- Request que reproduce el 500.
- Fragmento relevante del log/traceback.
- Causa raíz.
- Validación posterior.
- Evidencia de CORS para `http://localhost:3000`.

---

# VALIDACIÓN FINAL DEL EQUIPO

Cuando los cuatro integrantes terminen:

1. Integren los cambios.
2. Reinicien la API.
3. Ejecuten nuevamente los cuatro bloques de pruebas.
4. Confirmen que no rompieron los retos de otros compañeros.
5. Ejecuten el smoke test manual con curl/Postman.
6. Revisen los logs.
7. Registren los resultados.

---

# PUNTUACIÓN SUGERIDA

| Área | Puntos |
|---|---:|
| Reto 1 — REST/HTTP | 25 |
| Reto 2 — Headers/Auth/Validation | 25 |
| Reto 3 — Health/Dependency | 25 |
| Reto 4 — Logs/500/CORS | 25 |

En caso de empate, gana el equipo que complete antes la validación final con evidencia correcta.

---

# IMPORTANTE

El proyecto contiene fallos deliberados.

No todos los síntomas significan “error de código”.

Antes de cambiar archivos, utilicen evidencia:
- status HTTP,
- body,
- logs,
- headers,
- health checks,
- documentación Swagger,
- comportamiento de la dependencia.
