from abc import ABC, abstractmethod
from typing import List

from certx.common.model import models


class CertificateAuthorityService(ABC):
    @abstractmethod
    def create_certificate_authority(self, ca_option) -> models.PrivateCertificateAuthority:
        pass

    @abstractmethod
    def list_certificate_authorities(self, query_option=None) -> List[models.PrivateCertificateAuthority]:
        pass

    @abstractmethod
    def get_certificate_authority(self, ca_id) -> models.PrivateCertificateAuthority:
        pass

    @abstractmethod
    def delete_certificate_authority(self, ca_id):
        pass

    @abstractmethod
    def export_certificate_authority(self, ca_id) -> models.CertificateContent:
        pass
