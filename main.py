from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_database = []

# Aquí definimos lo que el servidor ESPERA recibir
class Cita(BaseModel):
    username: str
    hora: str
    mensaje: str   # <-- El error dice que esto faltaba

@app.post("/agendar/")
async def agendar_cita(cita: Cita):
    fake_database.append(cita.dict())
    return {"status": "ok", "recibido": cita}