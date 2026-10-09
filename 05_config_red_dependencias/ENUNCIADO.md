# Reto 5 — Configuración, red y dependencia

Tiempo: 30 minutos.

La API inicia y `/health/live` responde 200, pero `/health/ready` devuelve 503.

La aplicación depende del PostgreSQL ya creado en Azure.

Objetivo:
Determinar si la causa está en configuración, variables, DNS, puerto, autenticación, DB o código y conseguir `/health/ready` = 200.

Restricciones:
- No hardcodear secretos.
- No abrir PostgreSQL a todo Internet.
- No eliminar la comprobación real de DB.
