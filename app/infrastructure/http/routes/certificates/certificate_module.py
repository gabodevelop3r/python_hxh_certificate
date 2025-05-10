from app.infrastructure.http.controllers.certificate_controller import CertificateController
from .certificate_routes import get_certificate_routes
from app.application.services.certificates.get_certificate_service import GetCertificateService

# Instanciamos las dependencias (dependencia simple)
controller = CertificateController(GetCertificateService)

# Exportamos las rutas configuradas
certificate_router = get_certificate_routes(controller)
