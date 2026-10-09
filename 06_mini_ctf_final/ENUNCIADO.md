# Reto 6 — Mini CTF final

Tiempo: 60 minutos.

Un servicio de incidencias debe quedar operativo en Azure. El repositorio contiene varios problemas independientes.

Debe cumplir:
- GET /health/live -> 200 mientras el proceso esté vivo.
- GET /health/ready -> 200 solo si PostgreSQL responde; 503 si no.
- POST /api/incidents -> 201.
- GET /api/incidents -> 200.
- GET /api/incidents/{id} -> 200 o 404.
- GitHub Actions debe desplegar correctamente.
- Debe existir evidencia observable para diagnosticar fallos.

Restricciones:
- No crear nueva infraestructura.
- No hardcodear secretos.
- No abrir la DB a todo Internet.
- No resolver errores devolviendo siempre 200.
