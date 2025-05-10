# app/application/services/certificate_service.py
from app.domain.certificate.certificate import Certificate
from app.infrastructure.certificate_generator import CertificateGenerator

class CertificateService:
    def __init__(self, certificate_generator: CertificateGenerator):
        self.certificate_generator = certificate_generator

    def generate_certificate(self, data: Certificate) -> bytes:
        """
        Genera el certificado a partir de los datos recibidos.
        """
        return self.certificate_generator.generate(data)
