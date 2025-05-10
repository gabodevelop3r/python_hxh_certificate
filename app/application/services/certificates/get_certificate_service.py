from app.domain.certificate.get_certificate_service_interface import GetCertificateServiceInterface
from app.infrastructure.certificate_generator import CertificateGenerator

class GetCertificateService(GetCertificateServiceInterface):
    def __init__(self, certificate_generator: CertificateGenerator):
        self.certificate_generator = certificate_generator


    def get_certificate(self,certificate_id: int = None) -> dict:
       
       data = {
        'participant_name' : 'John Doe',
        'exam_code' : 'EXAM123',
        'score' : 95.0,
        'date' : '2023-10-01'
       } 

       return self.certificate_generator.generate(data)
