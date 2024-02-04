import os

from qpyone.compnents.storage.local_storage import LocalStorage, DictStorage
from qpyone.compnents.storage.s3_storage import S3Storage


def get_storage(api_key, data_dict):
    "get storage adapter configured in environment variables"
    mode = os.getenv('STORAGE_MODE', '').upper()
    path = os.getenv('STORAGE_PATH', '')
    if mode == 'S3':
        storage = S3Storage(api_key)
    elif mode == 'LOCAL':
        storage = LocalStorage(api_key, path)
    else:
        storage = DictStorage(api_key, data_dict)
    return storage
