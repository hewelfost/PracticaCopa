# Pack de Retos CTF — Hackathon Copa 2026

Contiene 6 retos independientes centrados en API, troubleshooting, observabilidad y despliegue Azure.

## Uso recomendado
- Trabaja un reto a la vez.
- Crea una rama por reto en el repo `Practica-de-Copa`.
- Copia el contenido del reto a la raíz de esa rama.
- No subas `.env` ni secretos.
- Para los retos Azure, reutiliza tu App Service y PostgreSQL existentes.
- No mezcles archivos de retos distintos.

# Reto 2 — API y HTTP bajo presión

## Descripción
Solución del Reto 2 para la Hackathon Copa 2026. Se realizó el refactor de una API REST basada en FastAPI para corregir las inconsistencias del contrato HTTP y asegurar el retorno de los códigos de estado apropiados según los estándares RESTful.

---

## Contrato HTTP Implementado

| Endpoint | Método | Estado HTTP Esperado | Descripción |
| :--- | :---: | :---: | :--- |
| `/health/live` | `GET` | `200 OK` | Verificación de estado de la API |
| `/api/tickets` | `POST` | `201 Created` | Creación de un nuevo ticket |
| `/api/tickets` | `GET` | `200 OK` | Obtención del listado completo de tickets |
| `/api/tickets/{id}` | `GET` | `200 OK` / `404 Not Found` | Obtención de un ticket específico por ID |
| `/api/tickets/{id}` | `PATCH` | `200 OK` / `404 Not Found` | Actualización parcial de datos de un ticket |
| `/api/tickets/{id}` | `DELETE` | `204 No Content` / `404 Not Found` | Eliminación de un ticket existente |

---

## Ejecución Local

### 1. Requisitos Previos
* Python 3.10+
* Entorno virtual de Python (`.venv`)

### 2. Instalación de Dependencias
```powershell
# Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# Instalar librerías
pip install -r requirements.txt