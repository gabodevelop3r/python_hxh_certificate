from fastapi import APIRouter
from app.infrastructure.http.controllers.certificate_controller import CertificateController
from app.application.services.certificates.get_certificate_service import GetCertificateService

from app.infrastructure.certificate_generator import CertificateGenerator
certificate_routes = APIRouter()


get_certificate_service = GetCertificateService(CertificateGenerator)

controller = CertificateController(get_certificate_service)

@certificate_routes.get("/{certificate_id}")
async def get_certificate(certificate_id: str):
    return await controller.get_certificate(certificate_id)

@certificate_routes.post("/")
def create_certificate():
    return controller.create_certificate()
