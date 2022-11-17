#!/usr/bin/env python
from typing import Type

from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlmodel import Session
from sqlmodel import SQLModel

from .models import DbConfig
from .utils import sql_result_to_model


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

    def exec(self, plain_sql: str, **kwargs):
        return self.query(plain_sql, **kwargs)

    def query_for_objects(self, plain_sql, result_type: type[BaseModel], **kwargs):
        result = self.query(plain_sql, **kwargs)
        return sql_result_to_model(result, result_type)

    def query_by_sqlmodel(self, plain_sql: str, **kwargs):
        with Session(self.engine) as session:
            st = text(plain_sql)
            result = session.execute(st, **kwargs)
        return result.all()

    def query_by_statement(self, statement):
        with Session(self.engine) as session:
            return session.execute(statement).all()
