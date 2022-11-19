#!/usr/bin/env python
# postgresql: postgresql: // scott: tiger @ localhost:5432 / mydatabase
# jdbc:postgresql://localhost:5432/mydatabase?currentSchema=myschema
# pip install psycopg2-binary
from typing import Optional

import pytest

from qpyone.clients.database.db_client import DbClient
from qpyone.clients.database.models import DbConfig
from qpyone.clients.database.utils import sql_result_to_model
from sqlmodel import Field
from sqlmodel import SQLModel
from sqlmodel import select


class Hero(SQLModel, table=True):
    __table_args__ = {"schema": "demo"}
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


def test_create_engine():
    db_config = DbConfig(url="postgresql://postgres:changeit@localhost:7432/test_hub")
    pg = DbClient(config=db_config)
    h1 = Hero(name="test3", secret_name="scret_name", age=10)
    pg.save(h1)

    statement = select(Hero).where(Hero.name == "test3")
    print(statement)
    result = pg.query_by_statement(statement)
    print(result)

    # SQLModel.metadata.create_all(pg.engine)
    # metadata = MetaData(schema="test_hub_demo")
    # metadata.create_all(pg.engine)


def test_query():
    sql = """
    select * from demo.hero
    """
    db_config = DbConfig(url="postgresql://postgres:changeit@localhost:7432/test_hub")
    pg = DbClient(config=db_config)
    raw_result = pg.exec(
        sql,
    )
    result = sql_result_to_model(raw_result, Hero)
    print(result)


def test_query_bind_params():
    sql = """
    select * from demo.hero where name=:name
    """
    db_config = DbConfig(url="postgresql://postgres:changeit@localhost:7432/test_hub")
    pg = DbClient(config=db_config)
    raw_result = pg.exec(sql, **{"name": "t2"})
    result = sql_result_to_model(raw_result, Hero)
    print(result)
