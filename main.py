from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# --- BASE DE DATOS SIMULADA (En memoria) ---
# Esto se borrará si reinicias el servidor
fake_database = []

# --- MODELO DE DATOS ---
class Cita(BaseModel):
    username: str
    schedule: str

# --- ENDPOINTS ---

@app.post("/agendar/")
def agendar_cita(cita: Cita):
    """
    Recibe los datos y simula guardarlos en la base de datos.
    """
    # Simulamos el guardado añadiendo a la lista
    fake_database.append(cita.dict())
    
    print(f"--> SIMULACIÓN DB: Se guardó horario de contacto para {cita.username} a las {cita.schedule}")
    
    return {
        "markdown": "...",
        "type": "markdown",
        "desc": f"¡Perfecto! Nos volveremos a contactar contigo durante las *{cita.schedule}*"
    }

@app.get("/ver-citas/")
def ver_citas():
    """
    Muestra lo que hay actualmente en la 'base de datos'.
    """
    return {"total_citas": len(fake_database), "citas": fake_database}

# Para correrlo: uvicorn main:app --reload