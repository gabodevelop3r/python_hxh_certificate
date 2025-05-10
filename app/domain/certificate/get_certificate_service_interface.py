from abc import ABC, abstractmethod

class GetCertificateServiceInterface(ABC):

    @abstractmethod
    def get_certificate(self, certificate_id: str) -> str:
        pass