from fastapi import APIRouter
from app.infrastructure.http.routes.certificates.certificate_routes import certificate_routes

# Creamos un router general para todas las rutas de la API
api_router = APIRouter()
api_router.include_router(certificate_routes, prefix="/certificates", tags=["Certificates"])