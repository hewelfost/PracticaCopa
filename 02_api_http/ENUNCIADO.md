# Reto 2 — API y HTTP bajo presión

Tiempo: 35 minutos.

La API inicia, pero varias operaciones no cumplen el contrato esperado.

Contrato:
- POST /api/tickets -> 201
- GET /api/tickets -> 200
- GET /api/tickets/{id} -> 200 o 404
- PATCH /api/tickets/{id} -> 200 o 404
- DELETE /api/tickets/{id} -> 204 o 404
- GET /health/live -> 200

Objetivo: hacer que la API cumpla exactamente ese contrato.

Entregables:
- Pruebas con Swagger/curl.
- Códigos correctos.
- Commit descriptivo.
