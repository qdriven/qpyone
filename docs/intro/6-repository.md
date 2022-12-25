# Repository Pattern

```python
"""
This is Python implementation of Repository pattern for accessing Data model
in an Object Oriented manner, simulating collection interface and abstracting
persistence operations.
The Repository also has Factory method for dealing with different Databases. Another
approach is to add direct engine string ingestion to the Repository __init__ method.
"""

from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class RepositoryInterface(ABC):
    def create(self, *args, **kwargs):
        raise NotImplemented()

    def list(self):
        raise NotImplemented()

    def get(self, id_):
        raise NotImplemented()

    def update(self, **fields):
        raise NotImplemented()

    def delete(self, id_):
        raise NotImplemented()


class Repository(RepositoryInterface):
    def __init__(self, model_cls):
        engine = self.engine_factory()
        self.session = Session(bind=engine)
        self.model_cls = model_cls

    def create(self, *args, **kwargs):
        obj = self.model_cls(*args, **kwargs)
        self.session.add(obj)
        self.session.commit()

    def list(self):
        return list(self.session.query(self.model_cls).order_by(self.model_cls.id))

    def get(self, id_):
        return self.session.query(self.model_cls).get(id_)

    def update(self, id_, **fields):
        obj = self.get(id_)
        for field, value in fields.items():
            obj.__setattr__(field, value)
        self.session.commit()

    def delete(self, id_):
        self.session.delete(self.get(id_))

    def engine_factory(self):
        # Factory method
        raise NotImplemented()


class SQLiteRepository(Repository):
    def engine_factory(self):
        return create_engine('sqlite:///:memory:', echo=True)


class MySQLRepository(Repository):
    def engine_factory(self):
        return create_engine('mysql://scott:tiger@localhost/foo', echo=True)


class PostgresRepository(Repository):
    def engine_factory(self):
        return create_engine('postgresql://scott:tiger@localhost/mydatabase', echo=True)
```


https://dddinpython.com/index.php/2022/09/23/implementing-the-repository-pattern/
https://github.com/ets-labs/python-dependency-injector
https://betterprogramming.pub/the-database-is-not-the-most-important-part-b87d8af01959
https://sqlalchemy-utils.readthedocs.io/en/latest/
https://programmingwithmosh.com/net/common-mistakes-with-the-repository-pattern/
https://www.fastapitutorial.com/
https://klaviyo.tech/managing-complexity-with-architecture-patterns-in-python-626b895710ca
https://codingcanvas.com/hexagonal-architecture/
https://www.reddit.com/r/Python/comments/w3yx00/design_pattern_using_the_repository_pattern_for/
https://io.made.com/
https://florian-kromer.medium.com/fastapi-microservice-patterns-domain-driven-design-e99f6f475691
https://github.com/faif/python-patterns
https://github.com/Miksus/red-bird
https://github.com/jiannei/lumen-api-starter
https://lyz-code.github.io/blue-book/
https://hackersandslackers.com/
https://github.com/hackersandslackers
https://death.andgravity.com/

```python
class XRepository(BaseRepository):
  model = X


class YRepository(BaseRepository):
  model = Y
class BaseRepository:

  @classmethod
  def get(cls):
    return cls.model.query.filter(...)
```
