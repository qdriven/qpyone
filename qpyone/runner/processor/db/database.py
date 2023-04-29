from dataclasses import dataclass

from injector import inject
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


@inject
@dataclass
class Database:
    ##TODO: need to seperate setting
    engine = create_engine(
        settings.DATABASE_URL, connect_args={"check_same_thread": False}
    )
    db_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()


class CustomBase(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)


# metadata = MetaData(
#     naming_convention={
#         "ix": "ix_%(column_0_label)s",
#         "uq": "uq_%(table_name)s_%(column_0_name)s",
#         "ck": "ck_%(table_name)s_%(constraint_name)s",
#         "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
#         "pk": "pk_%(table_name)s",
#     }
# )
# #
#
# @asynccontextmanager
# async def database_context():
#     await connect_database()
#     yield database
#     await disconnect_database()
#
#
# async def connect_database():
#     await database.connect()
#
#
# async def disconnect_database():
#     await database.disconnect()
#
#
# def init_database() -> None:
#     import todolist.infra.database.models  # noqa: F401
#
#     metadata.bind = create_engine(_SETTINGS.DATABASE_PG_URL)
#
#
# async def truncate_database() -> None:
#     await database.execute(
#         """TRUNCATE {} RESTART IDENTITY""".format(
#             ",".join(f'"{table.name}"' for table in reversed(metadata.sorted_tables))
#         )
#     )
