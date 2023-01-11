# Pytest 

## 命令行运行方式

- 运行文件
```shell
pytest test_file.py
```

- 运行目录
```shell
pytest folder/
```

- 运行方法

```shell
pytest test_mod.py::test_func 
pytest test_mod.py::TestClass::test_method

```

- run marker

```shell
pytest -m slow
```

- run package

```shell
pytest --pyargs pkg.testing
```
