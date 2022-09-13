#!/usr/bin/env python
# https://chartio.com/resources/tutorials/how-to-execute-raw-sql-in-sqlalchemy/
# metadata = MetaData()
# books = Table('book', metadata,
#   Column('id', Integer, primary_key=True),
#   Column('title', String),
#   Column('primary_author', String),
# )
#
# engine = create_engine('sqlite:///bookstore.db')
# metadata.create_all(engine)
# inspector = inspect(engine)
# inspector.get_columns('book')
# from sqlalchemy.sql import text
# with engine.connect() as con:
#
#     data = ( { "id": 1, "title": "The Hobbit", "primary_author": "Tolkien" },
#              { "id": 2, "title": "The Silmarillion", "primary_author": "Tolkien" },
#     )
#
#     statement = text("""INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)""")
#
#     for line in data:
#         con.execute(statement, **line)
#
# with engine.connect() as con:
#
#     rs = con.execute('SELECT * FROM book')
#
#     for row in rs:
#         print row
#
# Out[*]:
# (4, u'The Hobbit', u'Tolkien')
# (5, u'The Silmarillion', u'Tolkien')
