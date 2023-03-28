### JSON,Dict,Class,Yaml
<br>

JSON,Dict,Class统一看:

- 结构化数据
- key:value
- 字段:值

---

## 代码
<br>

<div class="grid grid-cols-3 gap-x-4">

<div>

#### JSON

```python
{
   "name": "China",
   "population": 1431002651,
   "capital": "Beijing",
   "languages": [
      "Chinese"
   ]
}
```
</div>

<div>

#### Dict

```python
 {
    "name": "United States",
    "population": 331002651,
    "capital": "Washington D.C.",
    "languages": [
        "English",
        "Spanish"
    ]
}
```
</div>

<div>

#### data class

```python
class Country(BaseModel):
    name: str
    population: int
    languages: List[str]
    capital: str
```

</div>

</div>

<br>

- class 附带了类型
- 其他三种基本认为表达的意思一样

---

### JSON,Dict,Dataclass

**三种可以相互转换**:
  
```python

c = Country(name="China", population=145565443, languages=["Chinese"])
print(c.json(),c.dict())
print(Country.parse_obj(dict_demo))
print(Country.parse_raw(json_str))

```

<br>

how about yaml? same? 都是结构化数据

---

### YAML 处理

- 和json一样,load/loads/dump/dumps
- 转化为data 类
- 和字典也是一样

--- 

### Pydantic-Yaml

**pydantic-yaml**使用,和JSON没有本质区别:

```python
class YamlGenericModel(YamlModel, extra=Extra.allow):
    pass


def load_yaml(file_path: str) -> Any:
    return YamlGenericModel.parse_file(file_path).dict()


def to_yaml_file(file_path: str, data: Union[YamlGenericModel, Dict]):
    if isinstance(data, YamlGenericModel):
        yaml_str = data.yaml()
    else:
        yaml_str = YamlGenericModel.parse_obj(data).yaml()
    with open(file_path, "w") as f:
        f.write(yaml_str)
```
