# SQL, ORM处理
https://www.cosmicpython.com/book/part1.html
https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make
https://adamj.eu/
https://itecnote.com/tecnote/python-implementation-of-repository-pattern-in-python/
https://red-bird.readthedocs.io/en/latest/
https://techspot.zzzeek.org/2012/02/07/patterns-implemented-by-sqlalchemy/


- 使用sqlalchemy/SQL model进行数据库操操作

## 初始化db

直接通过db的连接川初始化:
```python
db_config = DbConfig(url="postgresql://postgres:changeit@localhost:7432/test_hub")
pg = DbClient(config=db_config)
```

## 直接SQL语句操作

- 直接执行SQL,然后在将sql转化为定义的model

```python
   sql = """
    select * from demo.hero;
    """
    db_config = DbConfig(url="postgresql://postgres:changeit@localhost:7432/test_hub")
    pg = DbClient(config=db_config)
    raw_result = pg.exec(sql,)
    result = sql_result_to_model(raw_result,Hero)
    print(result)
```
- 执行带变量的sql

```python
    db_config = DbConfig(url="postgresql://postgres:changeit@localhost:7432/test_hub")
    pg = DbClient(config=db_config)
    raw_result = pg.exec(sql, **{'name': 't2'})
    result = sql_result_to_model(raw_result, Hero)
    print(result)
```

- 使用SQLModel进行查询和保存操作

直接给值，保存数据库：
```python
   db_config = DbConfig(url="postgresql://postgres:changeit@localhost:7432/test_hub")
    pg = DbClient(config=db_config)
    h1 = Hero(name="test2", secret_name="scret_name", age=10)
    pg.save(h1)
```

- 使用SQLModel方式查询

```python
statement = select(Hero).where(Hero.name == "test3")
    print(statement)
    result = pg.query_by_statement(statement)
    print(result)
```
