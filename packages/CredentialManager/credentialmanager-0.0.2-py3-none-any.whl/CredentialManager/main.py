import sys
import maskpass
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes


class CredentialManager(object):
    def __init__(self, **kwargs):
        self.bytes: int = 16
        self.password = kwargs.get('password', '-1').encode()
        self.aes_key = get_random_bytes(self.bytes)
        self.hmac_key = get_random_bytes(self.bytes)
        self.cipher = AES.new(self.aes_key, AES.MODE_CTR)
        self.hmac = HMAC.new(self.hmac_key, digestmod=SHA256)
        self.ciphertext = self.cipher.encrypt(self.password)
        self.tag = self.hmac.update(self.cipher.nonce + self.ciphertext).digest()
        self.secret_key = kwargs.get('secret_key', '-1')
        self.file_path = kwargs.get('file_path', '-1')

    def encrypt_password(self):
        # If file path is not given then create secret_key, else file path is given, write to file, then read and return
        if self.file_path == "-1":
            _secret_key = self.aes_key + self.hmac_key + self.tag + self.cipher.nonce + self.ciphertext
            return _secret_key
        else:
            with open(self.file_path, "wb") as file:
                file.write(self.aes_key)
                file.write(self.hmac_key)
                file.write(self.tag)
                file.write(self.cipher.nonce)
                file.write(self.ciphertext)

            with open(self.file_path, "rb") as file:
                _secret_key = file.read()
            return self.file_path

    def decrypt_password(self, **kwargs):
        """
        Expects string of secret_key data, or provide the full path to the key.bin that has the data to be read in.
        :param kwargs:
        :return:
        """

        if self.secret_key != "-1" and self.file_path == "-1":
            length = len(self.secret_key)
            k1 = slice(0, 16)  # key.read(16))
            k2 = slice(16, 32)  # key.read(16))
            k3 = slice(32, 64)  # key.read(32))
            k4 = slice(64, 72)  # key.read(8))
            k5 = slice(72, length)  # key.read())
            """
            k1 = slice(0, self.bytes)  # key.read(16))
            k2 = slice(self.bytes, 2 * self.bytes)  # key.read(16))
            k3 = slice(2 * self. bytes, 4 * self.bytes)  # key.read(32))
            k4 = slice(4 * self.bytes, 4 * self.bytes + 0.5 * self.bytes)  # key.read(8))
            k5 = slice(4 * self.bytes + 0.5 * self.bytes, length)  # key.read())
            """

            _aes_key = self.secret_key[k1]
            _hmac_key = self.secret_key[k2]
            tag = self.secret_key[k3]
            nonce = self.secret_key[k4]
            ciphertext = self.secret_key[k5]
        elif self.secret_key == "-1" and self.file_path != "-1":
            with open(self.file_path, "rb") as f:
                _aes_key = f.read(16)
                _hmac_key = f.read(16)
                tag = f.read(32)
                nonce = f.read(8)
                ciphertext = f.read()
        else:
            print("file path or secret_key data not provided.")
            sys.exit(1)

        try:
            hmac = HMAC.new(_hmac_key, digestmod=SHA256)
            tag = hmac.update(nonce + ciphertext).verify(tag)
        except ValueError:
            print("The message was modified!")
            sys.exit(1)

        cipher = AES.new(_aes_key, AES.MODE_CTR, nonce=nonce)
        message = cipher.decrypt(ciphertext)
        return message.decode()

    def create_key(self):
        self.password = maskpass.askpass(mask="*")
        _secret_key = CredentialManager(password=self.password).encrypt_password()
        return _secret_key

    def use_key(self):
        if self.secret_key == "-1" and self.file_path != "-1":
            decrypted_password = CredentialManager(file_path=self.file_path).decrypt_password()
        elif self.secret_key != "-1" and self.file_path == "-1":
            decrypted_password = CredentialManager(secret_key=self.secret_key).decrypt_password()
        else:
            decrypted_password = "-1"
        return decrypted_password


def main():
    """
    TODO: update scirpts and logic for better handling.  Right now it all passes into CredentialManager(),
    move so that encrypt_password(password, file_path) and decrypt_password(password, file_path)
    :return:
    """
    original_password = "SuperSecretPassword"
    print(f'original_password: {original_password}')
    secret_key = CredentialManager(password=original_password).encrypt_password()
    print(f'secret_key: {secret_key}')
    plain_text_password = CredentialManager(secret_key=secret_key).decrypt_password()
    print(f'plain_text_password: {plain_text_password}')


if __name__ == '__main__':
    main()
