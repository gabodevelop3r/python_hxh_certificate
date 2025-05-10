from fastapi import HTTPException
from typing import List, Dict
from app.domain.certificate.get_certificate_service_interface import GetCertificateServiceInterface

class CertificateController:
    def __init__(self, get_certificates_service: GetCertificateServiceInterface):
        self.get_certificates_service = get_certificates_service

    async def get_certificate(self, certificate_id: str) -> List[Dict]:
        try:
            certificates = self.get_certificates_service.get_certificates()
            return certificates
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener los certificados: {str(e)}")

