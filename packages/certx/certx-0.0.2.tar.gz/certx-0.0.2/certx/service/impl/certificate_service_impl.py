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
from certx.service.certificate_service import CertificateService
from certx.utils import algorithm_util
from certx.utils.crypto import x509_tools
from certx.utils import filter_util, generator

logger = logging.getLogger(__name__)


class CertificateServiceImpl(CertificateService):
    dbapi = db_api.get_instance()

    def __init__(self, **kwargs):
        pass

    def create_certificate(self, cert_option) -> models.PrivateCertificate:
        issue_id = cert_option.get('issue_id')
        db_ca = self._get_ca(issue_id)

        # Load CA
        resource_service = service.get_resource_service(db_ca.uri)
        ca_resource = resource_service.load_certificate(db_ca.uri)
        ca_cert = x509_tools.load_pem_x509_certificate(ca_resource.certificate_data)

        _ca_key_provider = key.get_key_provider(models.KeyAlgorithm(db_ca.key_algorithm))
        ca_key = _ca_key_provider.load_private_key(ca_resource.private_key_data,
                                                   password=crypto.decrypt(db_ca.password))

        key_algorithm = cert_option.get('key_algorithm') if cert_option.get(
            'key_algorithm') else models.KeyAlgorithm(db_ca.key_algorithm)
        signature_algorithm = cert_option.get('signature_algorithm') if cert_option.get(
            'signature_algorithm') else models.SignatureAlgorithm(db_ca.signature_algorithm)

        if not algorithm_util.validate_key_and_signature_algorithm(key_algorithm, signature_algorithm):
            msg = 'unmatched key_algorithm {} and signature_algorithm {}'.format(
                key_algorithm.value, signature_algorithm.value)
            logger.error(msg)
            raise exceptions.InvalidParameterValue(msg)

        # Generate certificate
        _cert_key_provider = key.get_key_provider(key_algorithm)
        cert_key = _cert_key_provider.generate_private_key()

        # DN
        cert_dn_option = cert_option.get('distinguished_name')
        cert_dn_country = cert_dn_option.get('country')
        cert_dn_state = cert_dn_option.get('state')
        cert_dn_locality = cert_dn_option.get('locality')
        cert_dn_organization = cert_dn_option.get('organization')
        cert_dn_organization_unit = cert_dn_option.get('organization_unit')
        cert_dn = models.DistinguishedName(
            common_name=cert_dn_option.get('common_name'),
            country=cert_dn_country if cert_dn_country else db_ca.country,
            state=cert_dn_state if cert_dn_state else db_ca.state,
            locality=cert_dn_locality if cert_dn_locality else db_ca.locality,
            organization=cert_dn_organization if cert_dn_organization else db_ca.organization,
            organization_unit=cert_dn_organization_unit if cert_dn_organization_unit else db_ca.organization_unit)

        # Generate CSR
        server_csr = x509_tools.generate_csr(cert_key, cert_dn.build_subject(), signature_algorithm.to_alg())

        cert_validity = models.Validity(**cert_option.get('validity'))
        not_before = datetime.fromtimestamp(
            cert_validity.start_from, timezone.utc) if cert_validity.start_from is not None else timeutils.utcnow()
        not_after = not_before + cert_validity.get_effective_time()

        # Generate Certificate
        cert = x509_tools.generate_certificate(server_csr.subject, ca_cert.subject, ca_key,
                                               server_csr.public_key(), signature_algorithm.to_alg(),
                                               not_before, not_after)

        # Save certificate and private key
        key_pass = generator.gen_password()
        cert_uri = resource_service.save_certificate(
            models.CertificateResourceType.CERTIFICATE,
            cert.public_bytes(Encoding.PEM),
            _cert_key_provider.get_private_bytes(cert_key, password=key_pass))

        cert_values = {
            'status': models.CaStatus.ISSUE.value,
            'issuer_id': db_ca.id,
            'key_algorithm': key_algorithm.value,
            'signature_algorithm': signature_algorithm.value,
            'serial_number': str(ca_cert.serial_number),
            'not_before': not_before,
            'not_after': not_after,
            'common_name': cert_dn.common_name,
            'country': cert_dn.country,
            'state': cert_dn.state,
            'locality': cert_dn.locality,
            'organization': cert_dn.organization,
            'organization_unit': cert_dn.organization_unit,
            'uri': cert_uri,
            'password': crypto.encrypt(key_pass)
        }

        try:
            db_cert = self.dbapi.create_certificate(cert_values)
        except Exception as e:
            logger.error('Save certificate failed, delete resource file %s...', cert_uri, e)
            resource_service.delete_certificate(cert_uri)
            raise exceptions.ServiceException('Create certificate failed')

        return models.PrivateCertificate.from_db(db_cert)

    def list_certificates(self, query_option=None):
        if query_option is None:
            query_option = {}

        filters = filter_util.build_filters(query_option,
                                            ['issuer_id', 'common_name', 'key_algorithm', 'signature_algorithm'])
        return [models.PrivateCertificate.from_db(ca) for ca in
                self.dbapi.get_certificates(filters=filters,
                                            limit=query_option.get('limit'),
                                            marker=query_option.get('marker'),
                                            sort_key=query_option.get('sort_key'),
                                            sort_dir=query_option.get('sort_dir'))]

    def get_certificate(self, cert_id) -> models.PrivateCertificate:
        db_cert = self.dbapi.get_certificate(cert_id)
        if db_cert is None:
            logger.error('certificate %s not found', cert_id)
            raise exceptions.NotFoundException('certificate {} not found'.format(cert_id))
        return models.PrivateCertificate.from_db(db_cert)

    def delete_certificate(self, cert_id):
        cert = self.get_certificate(cert_id)

        logger.info('Delete certificate {}'.format(cert_id))
        self.dbapi.destroy_certificate(cert_id)

        logger.info('Delete certificate {} resource with uri {}'.format(cert_id, cert.uri))
        try:
            service.get_resource_service(cert.uri).delete_certificate(cert.uri)
        except exceptions.CertificateResourceNotFound:
            pass

    def _get_ca(self, issuer_id):
        ca_model = self.dbapi.get_certificate_authority(issuer_id)
        if not ca_model:
            logger.error('CA %s not found.', issuer_id)
            raise exceptions.NotFoundException('CA {} not found.'.format(issuer_id))
        return ca_model

    def export_certificate(self, cert_id, export_option) -> models.CertificateContent:
        cert = self.get_certificate(cert_id)
        db_ca = self._get_ca(cert.issue_id)

        cert_resource = service.get_resource_service(cert.uri).load_certificate(cert.uri)

        _cert_key_provider = key.get_key_provider(cert.key_algorithm)
        cert_key = _cert_key_provider.load_private_key(cert_resource.private_key_data,
                                                       password=crypto.decrypt(cert.password))

        user_pass = export_option.get('password')

        ca_resource = service.get_resource_service(db_ca.uri).load_certificate(db_ca.uri)
        return models.CertificateContent(
            certificate=cert_resource.certificate_data,
            private_key=_cert_key_provider.get_private_bytes(cert_key, password=user_pass),
            certificate_chain=[ca_resource.certificate_data])
