from app.domain.certificate.get_certificate_service_interface import GetCertificateServiceInterface
from app.infrastructure.reporting.pdf.certificate_generator import CertificateGenerator
from app.domain.certificate.certificate import Certificate



class GenerateCertificateUseCase(GetCertificateServiceInterface):
    def __init__(self, certificate_generator: CertificateGenerator):
        self.certificate_generator = certificate_generator

    def get_certificate(self,certificate_id: int = None) -> dict:
       
        certificate_data = Certificate(**{
            'participant_name': 'John Doe',
            'exam_code': 'EXAM123',
            'score': 95.0,
            'date': '2023-10-01'
        })

        return self.certificate_generator.generate(certificate_data)
