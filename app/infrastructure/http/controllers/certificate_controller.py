from fastapi import HTTPException
from fastapi.responses import FileResponse
from typing import List, Dict
from app.domain.certificate.get_certificate_service_interface import GetCertificateServiceInterface
import os

class CertificateController:
    def __init__(self, get_certificates_service: GetCertificateServiceInterface):
        self.get_certificates_service = get_certificates_service

    async def get_certificate(self, certificate_id: str) -> List[Dict]:
        try:
            certificate_path = self.get_certificates_service.get_certificate()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener los certificados: {str(e)}")

        return FileResponse(
            path=certificate_path,
            media_type='application/pdf',
            filename=os.path.basename(certificate_path),
            headers={"Content-Disposition": f'inline; filename={os.path.basename(certificate_path)}'}
        )


