# app/interfaces/certificate_controller.py
from fastapi import APIRouter
from app.application.services.certificate_service import CertificateService
from app.domain.certificate import Certificate

router = APIRouter()

@router.post("/generate-certificate")
async def generate_certificate(data: Certificate):
    certificate_service = CertificateService(certificate_generator=CertificateGenerator())
    certificate_data = certificate_service.generate_certificate(data)
    return certificate_data
