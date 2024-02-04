"Storage adapter - one folder for each user / api_key"

# pip install pycryptodome
# REF: https://www.pycryptodome.org/src/cipher/aes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from retry import retry

from binascii import hexlify, unhexlify
import hashlib
import pickle
import zlib
import os

# pip install boto3 for aws


SALT = unhexlify(os.getenv('STORAGE_SALT', '00'))


class Storage:
    "Encrypted object storage (base class)"

    def __init__(self, secret_key):
        k = secret_key.encode()
        self.folder = hashlib.blake2s(k, salt=SALT, person=b'folder',
                                      digest_size=8).hexdigest()
        self.passwd = hashlib.blake2s(k, salt=SALT, person=b'passwd',
                                      digest_size=32).hexdigest()
        self.AES_MODE = AES.MODE_ECB  # TODO: better AES mode ???
        self.AES_BLOCK_SIZE = 16

    def get(self, name, default=None):
        "get one object from the folder"
        safe_name = self.encode(name)
        data = self._get(safe_name)
        obj = self.deserialize(data)
        return obj

    def put(self, name, obj):
        "put the object into the folder"
        safe_name = self.encode(name)
        data = self.serialize(obj)
        self._put(safe_name, data)
        return data

    def list(self):
        "list object names from the folder"
        return [self.decode(name) for name in self._list()]

    def delete(self, name):
        "delete the object from the folder"
        safe_name = self.encode(name)
        self._delete(safe_name)

    # IMPLEMENTED IN SUBCLASSES
    def _put(self, name, data):
        ...

    def _get(self, name):
        ...

    def _delete(self, name):
        pass

    def _list(self):
        ...

    # # #

    def serialize(self, obj):
        raw = pickle.dumps(obj)
        compressed = self.compress(raw)
        encrypted = self.encrypt(compressed)
        return encrypted

    def deserialize(self, encrypted):
        compressed = self.decrypt(encrypted)
        raw = self.decompress(compressed)
        obj = pickle.loads(raw)
        return obj

    def encrypt(self, raw):
        cipher = AES.new(unhexlify(self.passwd), self.AES_MODE)
        return cipher.encrypt(pad(raw, self.AES_BLOCK_SIZE))

    def decrypt(self, encrypted):
        cipher = AES.new(unhexlify(self.passwd), self.AES_MODE)
        return unpad(cipher.decrypt(encrypted), self.AES_BLOCK_SIZE)

    def compress(self, data):
        return zlib.compress(data)

    def decompress(self, data):
        return zlib.decompress(data)

    def encode(self, name):
        return hexlify(name.encode('utf8')).decode('utf8')

    def decode(self, name):
        return unhexlify(name).decode('utf8')
