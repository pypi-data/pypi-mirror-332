from marshmallow import EXCLUDE, fields, Schema, validate
from marshmallow_enum import EnumField

from certx.common.model import models

distinguishedNameRegex = '[a-zA-Z0-9\u4e00-\u9fa5-_.,* ]+'
uuidRegex = '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'


class CaDistinguishedName(Schema):
    common_name = fields.String(required=True,
                                validate=validate.And(validate.Length(min=1, max=64),
                                                      validate.Regexp(distinguishedNameRegex)))
    country = fields.String(required=True, validate=validate.Regexp('[a-zA-Z]{2}'))
    state = fields.String(required=False,
                          validate=validate.And(validate.Length(min=1, max=128),
                                                validate.Regexp(distinguishedNameRegex)))
    locality = fields.String(required=False,
                             validate=validate.And(validate.Length(min=1, max=128),
                                                   validate.Regexp(distinguishedNameRegex)))
    organization = fields.String(required=False,
                                 validate=validate.And(validate.Length(min=1, max=64),
                                                       validate.Regexp(distinguishedNameRegex)))
    organization_unit = fields.String(required=False,
                                      validate=validate.And(validate.Length(min=1, max=64),
                                                            validate.Regexp(distinguishedNameRegex)))

    class Meta(object):
        unknown = EXCLUDE


class Validity(Schema):
    type = EnumField(models.ValidityType, missing=models.ValidityType.YEAR)
    value = fields.Integer(required=True)

    class Meta(object):
        unknown = EXCLUDE


class SortDir(EnumField):
    DESC = 'desc'
    ASC = 'asc'


class ListPrivateCertificateAuthorityParameter(Schema):
    common_name = fields.String(validate=validate.And(validate.Length(min=1, max=64),
                                                      validate.Regexp(distinguishedNameRegex)))
    key_algorithm = EnumField(models.KeyAlgorithm)
    signature_algorithm = EnumField(models.SignatureAlgorithm)
    limit = fields.Integer(missing=10, validate=validate.Range(min=0, max=100))
    marker = fields.String(validate=validate.Regexp(uuidRegex))
    sort_key = fields.String(missing='created_at',
                             validate=validate.OneOf(('created_at', 'common_name', 'not_after'),
                                                     labels=['Certificate Create Time', 'Certificate Common Name',
                                                             'Certificate Expired Time']))
    sort_dir = EnumField(SortDir, missing=SortDir.DESC)


class CreatePrivateCertificateAuthorityOption(Schema):
    type = EnumField(models.CaType, missing=models.CaType.ROOT)
    distinguished_name = fields.Nested(CaDistinguishedName, required=True)
    key_algorithm = EnumField(models.KeyAlgorithm, missing=models.KeyAlgorithm.RSA4096)
    signature_algorithm = EnumField(models.SignatureAlgorithm, missing=models.SignatureAlgorithm.SHA512)
    validity = fields.Nested(Validity, required=True)
    issuer_id = fields.String(required=False, validate=validate.Regexp(uuidRegex))
    key_usages = fields.List(EnumField(models.KeyUsage))

    class Meta(object):
        unknown = EXCLUDE


class CreatePrivateCertificateAuthorityRequestBody(Schema):
    certificate_authority = fields.Nested(CreatePrivateCertificateAuthorityOption, required=True)

    class Meta(object):
        unknown = EXCLUDE


class PrivateCertificateAuthorityContent(Schema):
    certificate = fields.String()
    certificate_chain = fields.List(fields.String())


class PrivateCertificateAuthority(Schema):
    id = fields.String()
    type = EnumField(models.CaType)
    status = EnumField(models.CaType)
    key_algorithm = EnumField(models.KeyAlgorithm)
    signature_algorithm = EnumField(models.SignatureAlgorithm)
    distinguished_name = fields.Nested(CaDistinguishedName)
    not_before = fields.DateTime()
    not_after = fields.DateTime()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class ListPrivateCertificateParameter(Schema):
    issuer_id = fields.String(validate=validate.Regexp(uuidRegex))
    name = fields.String(validate=validate.And(validate.Length(min=1, max=64),
                                               validate.Regexp(distinguishedNameRegex)))
    key_algorithm = EnumField(models.KeyAlgorithm)
    signature_algorithm = EnumField(models.SignatureAlgorithm)
    limit = fields.Integer(missing=10, validate=validate.Range(min=0, max=1000))
    marker = fields.String(validate=validate.Regexp(uuidRegex))
    sort_key = fields.String(missing='created_at',
                             validate=validate.OneOf(('created_at', 'common_name', 'not_after'),
                                                     labels=['Certificate Create Time', 'Certificate Common Name',
                                                             'Certificate Expired Time']))
    sort_dir = EnumField(SortDir, missing=SortDir.DESC)


class CertDistinguishedName(Schema):
    common_name = fields.String(required=True,
                                validate=validate.And(validate.Length(min=1, max=64),
                                                      validate.Regexp(distinguishedNameRegex)))
    country = fields.String(required=False, validate=validate.Regexp('[a-zA-Z]{2}'))
    state = fields.String(required=False,
                          validate=validate.And(validate.Length(min=1, max=128),
                                                validate.Regexp(distinguishedNameRegex)))
    locality = fields.String(required=False,
                             validate=validate.And(validate.Length(min=1, max=128),
                                                   validate.Regexp(distinguishedNameRegex)))
    organization = fields.String(required=False,
                                 validate=validate.And(validate.Length(min=1, max=64),
                                                       validate.Regexp(distinguishedNameRegex)))
    organization_unit = fields.String(required=False,
                                      validate=validate.And(validate.Length(min=1, max=64),
                                                            validate.Regexp(distinguishedNameRegex)))

    class Meta(object):
        unknown = EXCLUDE


class PrivateCertificate(Schema):
    id = fields.String()
    status = EnumField(models.CertificateStatus)
    issuer_id = fields.String()
    key_algorithm = EnumField(models.KeyAlgorithm)
    signature_algorithm = EnumField(models.SignatureAlgorithm)
    distinguished_name = fields.Nested(CertDistinguishedName)
    not_before = fields.DateTime()
    not_after = fields.DateTime()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class CreatePrivateCertificateOption(Schema):
    issue_id = fields.String(required=True, validate=validate.Regexp(uuidRegex))
    distinguished_name = fields.Nested(CertDistinguishedName, required=True)
    key_algorithm = EnumField(models.KeyAlgorithm)
    signature_algorithm = EnumField(models.SignatureAlgorithm)
    validity = fields.Nested(Validity, required=True)
    issuer_id = fields.String(required=False, validate=validate.Length(min=36, max=36))
    key_usages = fields.List(EnumField(models.KeyUsage))

    class Meta(object):
        unknown = EXCLUDE


class CreatePrivateCertificateRequestBody(Schema):
    certificate = fields.Nested(CreatePrivateCertificateOption, required=True)

    class Meta(object):
        unknown = EXCLUDE


class ExportPrivateCertificateRequestBody(Schema):
    type = EnumField(models.DownloadType, default=models.DownloadType.OTHER)
    password = fields.String()

    class Meta(object):
        unknown = EXCLUDE


class PrivateCertificateContent(Schema):
    certificate = fields.String()
    private_key = fields.String()
    certificate_chain = fields.List(fields.String())
