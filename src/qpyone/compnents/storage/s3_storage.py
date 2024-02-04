# pip install boto3 for aws
import boto3
import botocore

from qpyone.compnents.storage.base import Storage
import io
import os
import boto3
import botocore


class S3Storage(Storage):
    "S3 based encrypted storage"

    def __init__(self, secret_key, **kw):
        prefix = kw.get('prefix') or os.getenv('S3_PREFIX', 'index/x1')
        region = kw.get('region') or os.getenv('S3_REGION', 'sfo3')
        bucket = kw.get('bucket') or os.getenv('S3_BUCKET', 'ask-my-pdf')
        url = kw.get('url') or os.getenv('S3_URL'
                                         , f'https://{region}.digitaloceanspaces.com')
        key = os.getenv('S3_KEY', '')
        secret = os.getenv('S3_SECRET', '')
        #
        if not key or not secret:
            raise Exception("No S3 credentials in environment variables!")
        #
        super().__init__(secret_key)
        self.session = boto3.session.Session()
        self.s3 = self.session.client('s3',
                                      config=botocore.config.Config
                                      (s3={'addressing_style': 'virtual'}),
                                      region_name=region,
                                      endpoint_url=url,
                                      aws_access_key_id=key,
                                      aws_secret_access_key=secret,
                                      )
        self.bucket = bucket
        self.prefix = prefix

    def get_key(self, name):
        return f'{self.prefix}/{self.folder}/{name}'

    def _put(self, name, data):
        key = self.get_key(name)
        f = io.BytesIO(data)
        self.s3.upload_fileobj(f, self.bucket, key)

    def _get(self, name):
        key = self.get_key(name)
        f = io.BytesIO()
        self.s3.download_fileobj(self.bucket, key, f)
        f.seek(0)
        return f.read()

    def _list(self):
        resp = self.s3.list_objects(
            Bucket=self.bucket,
            Prefix=self.get_key('')
        )
        contents = resp.get('Contents', [])
        contents.sort(key=lambda x: x['LastModified'], reverse=True)
        keys = [x['Key'] for x in contents]
        names = [x.split('/')[-1] for x in keys]
        return names

    def _delete(self, name):
        self.s3.delete_object(
            Bucket=self.bucket,
            Key=self.get_key(name)
        )
