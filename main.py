from fastapi import FastAPI
from app.infrastructure.http.routes import api_router

app = FastAPI()

# Incluimos las rutas en la aplicación principal
app.include_router(api_router)
