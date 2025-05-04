from app.infrastructure.certificate_generator import CertificateGenerator
from app.application.usecases.generate_certificate import GenerateCertificate
from app.application.services.certificate_service import CertificateService
from app.domain.certificate import Certificate


def run_cli():
    pdf_generator = CertificateGenerator()
    certificate_service = CertificateService(pdf_generator)
    use_case = GenerateCertificate(certificate_service)

    data_certificate = Certificate(
        participant_name="Gon Freecss",
        exam_code="12.345.678-9",
        score="100",
        date="01-06-2025",
    )
    output_path = use_case.execute(data_certificate)
    print(f"PDF generado en: {output_path}")
