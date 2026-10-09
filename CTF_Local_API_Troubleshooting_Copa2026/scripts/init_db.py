from pathlib import Path

from app.database import Base, engine, SessionLocal
from app.models import Incident

Path("data").mkdir(exist_ok=True)

Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    if db.query(Incident).count() == 0:
        db.add_all([
            Incident(
                title="VPN intermitente",
                description="Usuarios reportan desconexiones",
                priority="high",
            ),
            Incident(
                title="Impresora offline",
                description="La impresora de recepción no responde",
                priority="low",
            ),
        ])
        db.commit()
finally:
    db.close()

print("Base local inicializada.")
