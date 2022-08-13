#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine, text
from sqlmodel import SQLModel, Session

from fluentqpy.clients.database.models import DbConfig


class DbClient:

    def __init__(self, config: DbConfig):
        self.config = config
        self.engine = create_engine(url=config.url)

    @classmethod
    def create_engine(cls, connection_url):
        """
        postgresql: postgresql://scott:tiger@localhost:5432/mydatabase
        """

        return create_engine(connection_url)

    def save(self, instance: SQLModel):
        with Session(self.engine) as s:
            s.add(instance)
            s.commit()

    def query(self, plain_sql: str, **kwargs):
        s = text(plain_sql)
        with self.engine.connect() as conn:
            result = conn.execute(s, **kwargs)
        return result

    def query_by_sqlmodel(self, plain_sql: str, **kwargs):
        with Session(self.engine) as session:
            st = text(plain_sql)
            result = session.execute(st, **kwargs)
        return result
