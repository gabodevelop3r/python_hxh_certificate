from fastapi import APIRouter
from app.infrastructure.http.controllers.certificate_controller import CertificateController
from app.application.usecases.certificates.generate_certificate_usecase import GenerateCertificateUseCase

from app.infrastructure.reporting.pdf.certificate_generator import CertificateGenerator
certificate_routes = APIRouter()


generate_certificate_use_case = GenerateCertificateUseCase(CertificateGenerator)

controller = CertificateController(generate_certificate_use_case)

@certificate_routes.get("/{certificate_id}")
async def get_certificate(certificate_id: str):
    return await controller.get_certificate(certificate_id)

@certificate_routes.post("/")
def create_certificate():
    return controller.create_certificate()
