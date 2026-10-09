import logging
import os
from fastapi import FastAPI, Request, HTTPException
from time import perf_counter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("challenge")

connection_string = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")
if connection_string:
    from azure.monitor.opentelemetry import configure_azure_monitor
    configure_azure_monitor(connection_string=connection_string)

app = FastAPI(title="Observability Challenge")

@app.middleware("http")
async def request_logger(request: Request, call_next):
    started = perf_counter()
    response = await call_next(request)
    elapsed_ms = (perf_counter() - started) * 1000
    logger.info("%s %s -> %s %.2fms",
                request.method, request.url.path, response.status_code, elapsed_ms)
    return response

@app.get("/health/live")
def live():
    return {"status": "alive"}

@app.get("/api/calculate")
def calculate(value: int, divisor: int = 1):
    if divisor == 0:
        raise HTTPException(status_code=400, detail="El divisor no puede ser cero.")
    return {"result": value / divisor}

@app.get("/api/orders/{order_id}")
def order(order_id: int):
    if order_id == 13:
        raise HTTPException(status_code=404, detail="Orden no encontrada o datos inválidos.")
    return {"id": order_id, "status": "processed"}
