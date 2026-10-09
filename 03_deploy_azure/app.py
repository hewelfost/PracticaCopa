from fastapi import FastAPI
app = FastAPI(title="Deployment Challenge")

@app.get("/")
def root():
    return {"service": "deployment-challenge", "status": "running"}

@app.get("/health/live")
def live():
    return {"status": "alive"}
