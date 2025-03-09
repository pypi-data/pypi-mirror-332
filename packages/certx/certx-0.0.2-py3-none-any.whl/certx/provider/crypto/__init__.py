from . import password


def get_crypto():
    return password.DefaultPasswordEncoder()


def encrypt(row_data):
    return get_crypto().encrypt(row_data)


def decrypt(cipher_data):
    return get_crypto().decrypt(cipher_data)
