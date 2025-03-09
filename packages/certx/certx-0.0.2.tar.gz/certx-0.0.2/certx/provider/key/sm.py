from certx.common import exceptions
from certx.provider.key.base import KeyProvider


class SmKeyProvider(KeyProvider):
    def generate_private_key(self):
        raise exceptions.NotImplementException("GM algorithm not supported")

    def get_private_bytes(self, private_key, password: str = None):
        raise exceptions.NotImplementException()

    def load_private_key(self, private_key_bytes, password: str = None):
        raise exceptions.NotImplementException()
