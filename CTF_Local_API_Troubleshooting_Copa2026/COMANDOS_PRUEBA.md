# Comandos de prueba — NO son soluciones

Base local:

```text
http://127.0.0.1:8000
```

## General

```bash
curl -i http://127.0.0.1:8000/
curl -i http://127.0.0.1:8000/health/live
curl -i http://127.0.0.1:8000/health/ready
```

## Incidencias

```bash
curl -i http://127.0.0.1:8000/api/incidents
curl -i http://127.0.0.1:8000/api/incidents/1
curl -i http://127.0.0.1:8000/api/incidents/9999
```

Crear:

```bash
curl -i -X POST http://127.0.0.1:8000/api/incidents ^
  -H "Content-Type: application/json" ^
  -d "{\"title\":\"DNS falla\",\"description\":\"No resuelve nombres\",\"priority\":\"high\"}"
```

PowerShell puede usar `curl.exe` para evitar el alias de `Invoke-WebRequest`.

## Endpoint privado

Sin credenciales:

```bash
curl -i http://127.0.0.1:8000/api/private/summary
```

Con header:

```bash
curl -i http://127.0.0.1:8000/api/private/summary ^
  -H "X-API-Key: VALOR"
```

## Validación JSON

```bash
curl -i -X POST http://127.0.0.1:8000/api/private/echo ^
  -H "Content-Type: application/json" ^
  -d "{}"
```

## Reports

```bash
curl -i http://127.0.0.1:8000/api/reports/1
curl -i http://127.0.0.1:8000/api/reports/13
```

## CORS / preflight

```bash
curl -i -X OPTIONS http://127.0.0.1:8000/api/incidents ^
  -H "Origin: http://localhost:3000" ^
  -H "Access-Control-Request-Method: GET"
```

## Swagger

```text
http://127.0.0.1:8000/docs
```

Usen los comandos para observar, no para asumir la causa.
