from . import base
from . import ec
from . import rsa
from . import sm

from certx.common.model import models

_KEY_PROVIDER_MAP = {
    models.KeyAlgorithm.RSA2048: rsa.RsaKeyProvider,
    models.KeyAlgorithm.RSA3072: rsa.RsaKeyProvider,
    models.KeyAlgorithm.RSA4096: rsa.RsaKeyProvider,
    models.KeyAlgorithm.EC256: ec.EcKeyProvider,
    models.KeyAlgorithm.EC384: ec.EcKeyProvider,
    models.KeyAlgorithm.SM2: sm.SmKeyProvider,
}


def get_key_provider(key_algorithm: models.KeyAlgorithm):
    if key_algorithm not in _KEY_PROVIDER_MAP:
        raise NotImplemented

    return _KEY_PROVIDER_MAP.get(key_algorithm)(key_algorithm.value)
