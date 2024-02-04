from qpyone.compnents.storage.base import Storage

import os


class LocalStorage(Storage):
    "Local filesystem based storage"

    def __init__(self, secret_key, path):
        if not path:
            raise Exception('No storage path in environment variables!')
        super().__init__(secret_key)
        self.path = os.path.join(path, self.folder)
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def _put(self, name, data):
        with open(os.path.join(self.path, name), 'wb') as f:
            f.write(data)

    def _get(self, name):
        with open(os.path.join(self.path, name), 'rb') as f:
            data = f.read()
        return data

    def _list(self):
        # TODO: sort by modification time (reverse=True)
        return os.listdir(self.path)

    def _delete(self, name):
        os.remove(os.path.join(self.path, name))


class DictStorage(Storage):
    "Dictionary based storage"

    def __init__(self, secret_key, data_dict):
        super().__init__(secret_key)
        self.data = data_dict

    def _put(self, name, data):
        if self.folder not in self.data:
            self.data[self.folder] = {}
        self.data[self.folder][name] = data

    def _get(self, name):
        return self.data[self.folder][name]

    def _list(self):
        # TODO: sort by modification time (reverse=True)
        return list(self.data.get(self.folder, {}).keys())

    def _delete(self, name):
        del self.data[self.folder][name]
