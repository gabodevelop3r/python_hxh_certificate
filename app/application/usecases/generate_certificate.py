# app/application/usecases/generate_certificate.py
from app.application.services.certificate_service import CertificateService
from app.domain.certificate.certificate import Certificate

class GenerateCertificate:
    def __init__(self, certificate_service: CertificateService):
        self.certificate_service = certificate_service

    def execute(self, data: Certificate) -> bytes:
        """
        Casos de uso: Generar el certificado con la lógica del servicio.
        """
        return self.certificate_service.generate_certificate(data)
