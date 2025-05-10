from app.domain.certificate.certificate import Certificate
import os
from jinja2 import Template
from weasyprint import HTML

class CertificateGenerator:

    @staticmethod
    def generate(certificate_data: Certificate) -> str:

        template_path = os.path.join(os.path.dirname(__file__), '../../../templates/certificate.html')

        with open(template_path, 'r') as file:
            template_content = file.read()

        template = Template(template_content)

        rendered_html = template.render(
            participant_name=certificate_data.participant_name,
            exam_code=certificate_data.exam_code,
            score=certificate_data.score,
            date=certificate_data.date,
        )

        static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../static'))

        pdf = HTML(string=rendered_html, base_url=static_path).write_pdf()

        output_dir = os.path.join(os.path.dirname(__file__), '../output')
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f"{certificate_data.participant_name.replace(' ', '_')}_certificate.pdf")

        with open(output_path, 'wb') as f:
            f.write(pdf)

        return os.path.abspath(output_path)
