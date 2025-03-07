from collections.abc import Callable, Generator

from cryptography.fernet import Fernet

from fernet_encrypt.utils import api, key_getter, key_setter


def create_key(key_setter: Callable = key_setter):
    key = Fernet.generate_key()
    key_setter(key)


def encrypt(input: bytes, key_getter: Callable[[], Generator[bytes, None, None]] = key_getter) -> bytes:
    key = Fernet(next(key_getter()))
    return key.encrypt(input)


def decrypt(input: bytes, key_getter: Callable[[], Generator[bytes, None, None]] = key_getter) -> bytes:
    key_count = 0
    for key_str in key_getter():
        key = Fernet(key_str)
        key_count += 1

        try:
            decrypted_data = key.decrypt(input)
        except Exception:  # nosec: CWE-703
            continue

        return decrypted_data

    raise Exception(f"Unable to decrypt input with {key_count} existing keys.")


def remote_login(refresh_token: str | None = None):
    api.login(refresh_token=refresh_token)


def get_remote_keys() -> dict:
    return api.get_keys()


def decrypt_remote(input: bytes) -> bytes:
    return api.decrypt(input)


def encrypt_remote(input: bytes, name: str) -> bytes:
    return api.encrypt(input, name)
