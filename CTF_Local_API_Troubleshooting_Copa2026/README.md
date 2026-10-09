# Copa Incident Service — CTF local

Proyecto intencionalmente defectuoso para entrenamiento de:

- REST APIs
- HTTP status codes
- JSON
- curl
- Postman
- Swagger/OpenAPI
- headers
- autenticación simple
- validación
- health checks
- SQLite
- logs
- HTTP 500
- CORS
- troubleshooting
- Git/GitHub

## Requisitos
- Python 3.11+
- PowerShell, Bash o terminal
- curl o Postman

## Instalación

```bash
python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instalar:

```bash
pip install -r requirements.txt
```

Crear `.env`:

```powershell
Copy-Item .env.example .env
```

o:

```bash
cp .env.example .env
```

Inicializar datos locales:

```bash
python scripts/init_db.py
```

Ejecutar:

```bash
uvicorn app.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## Enunciado

Leer primero:

`ENUNCIADO.md`

## Recomendación de equipo

- Integrante 1 → `app/routers/incidents.py`
- Integrante 2 → `app/routers/private.py`
- Integrante 3 → `app/routers/health.py`
- Integrante 4 → `app/routers/reports.py` + CORS/logs

Los archivos compartidos deben modificarse con cuidado para no romper trabajo ajeno.
