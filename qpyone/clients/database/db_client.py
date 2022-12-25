#!/usr/bin/env python
from typing import Type

from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlmodel import Session
from sqlmodel import SQLModel
from sqlmodel import delete
from sqlmodel import select
from sqlmodel import update

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
            s.refresh(instance)

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

    def __query_by_statement(self, statement):
        with Session(self.engine) as session:
            return session.exec(statement).all()

    def _build_query(self, entity: SQLModel, **kwargs):
        return select(entity).filter_by(**kwargs)

    def _build_delete_statement(self, entity: SQLModel, **kwargs):
        return delete(entity).filter_by(**kwargs)

    def find_by(self, entity: type[SQLModel], **kwargs):
        query = self._build_query(entity, **kwargs)
        return self.__query_by_statement(query)

    def delete_by(self, entity: type[SQLModel], **kwargs):
        with Session(self.engine) as session:
            statement = self._build_delete_statement(entity, **kwargs)
            session.exec(statement)
            session.commit()

    def update_by(self, entity: type[SQLModel], instance: SQLModel):
        with Session(self.engine) as session:
            statement = (
                update(entity).filter_by(id=instance.id).values(**instance.dict())
            )
            session.exec(statement)
            session.commit()
