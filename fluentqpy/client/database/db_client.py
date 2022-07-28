#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

from fluentqpy.client.database.models import DbConfig


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
