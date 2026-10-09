import logging
from time import perf_counter

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import incidents, private, health, reports

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger("copa_ctf")

app = FastAPI(
    title="Copa Incident Service",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def request_logging(request: Request, call_next):
    started = perf_counter()
    try:
        response = await call_next(request)
        elapsed_ms = (perf_counter() - started) * 1000
        logger.info(
            "%s %s -> %s %.2fms",
            request.method,
            request.url.path,
            response.status_code,
            elapsed_ms,
        )
        return response
    except Exception:
        elapsed_ms = (perf_counter() - started) * 1000
        logger.exception(
            "%s %s -> EXCEPTION %.2fms",
            request.method,
            request.url.path,
            elapsed_ms,
        )
        raise

@app.get("/")
def root():
    return {
        "service": "Copa Incident Service",
        "status": "running",
        "docs": "/docs",
    }

app.include_router(incidents.router)
app.include_router(private.router)
app.include_router(health.router)
app.include_router(reports.router)
