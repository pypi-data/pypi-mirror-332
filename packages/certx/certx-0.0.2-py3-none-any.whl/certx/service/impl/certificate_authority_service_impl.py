from datetime import datetime, timezone

from cryptography.hazmat.primitives.serialization import Encoding
from oslo_log import log as logging
from oslo_utils import timeutils

from certx.common import exceptions
from certx.common.model import models
from certx.db import api as db_api
from certx.provider import crypto
from certx.provider import key
from certx import service
from certx.service.certificate_authority_service import CertificateAuthorityService
from certx.utils.crypto import x509_tools
from certx.utils import filter_util, generator

logger = logging.getLogger(__name__)


class CertificateAuthorityServiceImpl(CertificateAuthorityService):
    dbapi = db_api.get_instance()

    def __init__(self, **kwargs):
        pass

    def create_certificate_authority(self, ca_option) -> models.PrivateCertificateAuthority:
        key_algorithm = ca_option.get('key_algorithm')
        signature_algorithm = ca_option.get('signature_algorithm')
        logger.info('generate CA private key...')
        _key_provider = key.get_key_provider(key_algorithm)
        ca_key = _key_provider.generate_private_key()

        ca_dn = models.DistinguishedName(**ca_option.get('distinguished_name'))
        ca_subject = ca_dn.build_subject()
        ca_validity = models.Validity(**ca_option.get('validity'))
        not_before = datetime.fromtimestamp(
            ca_validity.start_from, timezone.utc) if ca_validity.start_from is not None else timeutils.utcnow()
        not_after = not_before + ca_validity.get_effective_time()

        logger.info('generate CA...')
        ca_cert = x509_tools.generate_ca_certificate(subject_name=ca_subject, root_key=ca_key, not_before=not_before,
                                                     not_after=not_after,
                                                     signature_algorithm=signature_algorithm.to_alg())

        key_pass = generator.gen_password()

        logger.info('generate CA resource...')
        resource_service = service.get_resource_service()
        ca_uri = resource_service.save_certificate(
            models.CertificateResourceType.CA,
            ca_cert.public_bytes(Encoding.PEM),
            _key_provider.get_private_bytes(ca_key, password=key_pass))

        ca_values = {
            'type': ca_option.get('type').value,
            'status': models.CaStatus.ISSUE.value,
            'path_length': 0,
            'issuer_id': None,
            'key_algorithm': key_algorithm.value,
            'signature_algorithm': signature_algorithm.value,
            'serial_number': str(ca_cert.serial_number),
            'not_before': not_before,
            'not_after': not_after,
            'common_name': ca_dn.common_name,
            'country': ca_dn.country,
            'state': ca_dn.state,
            'locality': ca_dn.locality,
            'organization': ca_dn.organization,
            'organization_unit': ca_dn.organization_unit,
            'uri': ca_uri,
            'password': crypto.encrypt(key_pass)
        }

        try:
            ca = self.dbapi.create_certificate_authority(ca_values)
        except Exception as e:
            logger.error('Save CA failed, delete resource file %s...', ca_uri, e)
            resource_service.delete_certificate(ca_uri)
            raise exceptions.ServiceException('Create CA failed')

        return models.PrivateCertificateAuthority.from_db(ca)

    def list_certificate_authorities(self, query_option=None):
        if query_option is None:
            query_option = {}

        filters = filter_util.build_filters(query_option, ['common_name', 'key_algorithm', 'signature_algorithm'])
        return [models.PrivateCertificateAuthority.from_db(ca) for ca in
                self.dbapi.get_certificate_authorities(filters=filters,
                                                       limit=query_option.get('limit'),
                                                       marker=query_option.get('marker'),
                                                       sort_key=query_option.get('sort_key'),
                                                       sort_dir=query_option.get('sort_dir'))]

    def get_certificate_authority(self, ca_id) -> models.PrivateCertificateAuthority:
        db_ca = self.dbapi.get_certificate_authority(ca_id)
        if db_ca is None:
            logger.error('CA {} not found'.format(ca_id))
            raise exceptions.ServiceException('CA {} not found'.format(ca_id))
        return models.PrivateCertificateAuthority.from_db(db_ca)

    def delete_certificate_authority(self, ca_id):
        ca = self.get_certificate_authority(ca_id)

        db_certs = self.dbapi.get_certificates(filters={'issuer_id': ca_id})
        if db_certs:
            logger.error('CA {} has signed certificate, could not be deleted'.format(ca_id))
            raise exceptions.CaSignedCertificate('CA {} has signed certificate, could not be deleted'.format(ca_id))

        logger.info('delete CA {}'.format(ca_id))
        self.dbapi.destroy_certificate_authority(ca_id)

        logger.info('delete CA {} resource with uri {}'.format(ca_id, ca.uri))
        try:
            service.get_resource_service(ca.uri).delete_certificate(ca.uri)
        except exceptions.CertificateResourceNotFound:
            pass

    def export_certificate_authority(self, ca_id) -> models.CertificateContent:
        ca = self.get_certificate_authority(ca_id)
        ca_resource = service.get_resource_service(ca.uri).load_certificate(ca.uri)
        return models.CertificateContent(certificate=ca_resource.certificate_data)
