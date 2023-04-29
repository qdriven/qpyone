# 关于JSON的所有

给测试同学说的JSON,目标:
1. 30分钟左右讲完所有JSON内容
2. 什么是JSON
   1. key-value
   2. array
3. JSON怎么用
   1. 读取写入JSON
   2. JSON和DICT的转换
   3. 获取JSON字段值
   4. JSON和类的转换
4. 比较两个类似JSON的差别

---

## 什么是JSON

- 什么是JSON,key-value对？

>JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式,JSON数据由键值对组成，其中键是**字符串**，值可以是字符串、数字、布尔值、数组、对象或null。
> 在JSON中，键值对是由冒号分隔的，每个键值对之间由逗号分隔。例如：
```json
{
  "name": "John",
  "age": 30,
  "isStudent": true,
  "hobbies": ["reading", "swimming", "traveling"],
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY"
  },
  "favoriteFoods": null
}
```

> 在上面的例子中，`name`、`age`、`isStudent`、`hobbies`、`address`和`favoriteFoods`都是键，它们的值分别是字符串、数字、布尔值、数组、对象和null。

---

## 有没有什么不同的JSON

<div class="grid grid-cols-2 gap-x-8">

<div>
并不完全是key-value,键值对:

##### json array

```json
[1, 2, 3, 4, 5]
```
</div>

<div>

##### 另一种JSON Array

<br>

```json
[
  {
    "name": "John",
    "age": 30
  },
  {
    "name": "Jane",
    "age": 25
  }
]
```

</div></div>

---

## JSON小结下

- 一种文本格式
- 大部分情况是key-value,键值对
   1. key,只能是string类型
   2. value,可以是很多类型
- json array，数组的形式

---

## 如何使用Python读取和写入JSON
<br>

#### 读取:输入/输出是什么？

- 输入: json字符串或者文件
- 输出: dict

```python
json_str = """
{
   "name": "China","population": 1431002651,"capital": "Beijing",
   "languages": [
      "Chinese"
   ]
}
"""
def json_to_dict() -> Dict:
    rich.print(type(json_str))
    rich.print_json(json_str)
    dict_demo = json.loads(json_str)
    return dict_demo
def read_json_file(file_name: str='country.json')->Dict:
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
```

---

#### 写入:输入/输出是什么？
<br>

- 输入是: 对象
- 输出是: JSON字符串或者直接写入问题
<br>
```python
dict_demo = {
    "name": "United States",
    "population": 331002651,
    "capital": "Washington D.C.",
    "languages": [
        "English",
        "Spanish"
    ]
}
def dict_to_json():
    return json.dumps(dict_demo, ensure_ascii=True)
def to_json_file(file_path: str):
    with open(file_path, 'w') as f:
        json.dump(dict_demo, f)
```

---

## JSON处理

<br>

- load/loads, 区别是什么
- dump/dumps,区别是什么

---

## 如何获取JSON中某个字段的值
<br>

- 读取JSON字符串转化成对象(dict/list)
- 使用dict的方法获取字段(key对应的值)
- 如果是list呢？那就用list的方式处理

```python
json.loads(json_str)["name"]
```
```python
json_array_str="[1,2,3,435]"

print(json.loads(json_array_str)[0])
```

问题: 封装一个统一处理json获取值的函数
1. 实现要load一个json字符串
2. 其次要考虑json可能会有嵌套情况

---

## json: jmeshpath使用

<br>

**jmeshpath**: 使用表达式就可以获取json字段值: ```students.name```

- 例子：

```python
for_extract_str = {
    "name": "China",
    "population": 1431002651,
    "capital": "Beijing",
    "languages": [
        "Chinese"
    ],"students": {
        "name": "name",
        "age":18
    }
}

def get_value(json_str: Dict, path_exp: str) -> Any:
    return jmespath.search(expression=path_exp, data=json_str)

get_value(json_str=for_extract_str, path_exp="students.name")
```

---

## 改变JSON值
<br>

- 参考字典改变值的方式
- 使用 **dotty**修改值,通过表达式的方式
  
```python
def set_value(json_dict: Dict, path_exp: str, to_value: Any) -> Dict:
    dot = dotty(json_dict)
    dot[path_exp] = to_value
    return dot.to_dict()

set_value(json_dict=for_extract_str, path_exp="students.name",
                     to_value="Niu")
```

---

## 如何使用JSON和类转换
<br>

**使用pydantic**:

- parse_raw/json 两个方法就可以相互转换
- 方便编写代码,IDE自动提示字段,大量减少```dict[key]```这样的代码

--- 

## 如何使用JSON和类转换-Pydantic

<br>

```python
class Country(BaseModel):
    name: str
    population: int
    languages: List[str]
json_str = """
{
   "name": "China",
   "population": 1431002651,
   "capital": "Beijing",
   "languages": [
      "Chinese"
   ]
}
"""
c =Country.parse_raw(json_str)
print(c.json())
```
---

### 如何比较JSON的差别

**使用Deepdiff**: 满足日常使用

```python
t1 = {1: 1, 2: 2, 3: 3}
t2 = {1: 1, 2: "2", 3: 3}

different_result = DeepDiff(t1, t2, verbose_level=0)

for key, item in different_result.items():
    print("change_type", key)
    print("change_details:")
    for element in item.values():
        print(element)

```

---

## Diff JSON 复杂场景

```python
json_str = """
{
   "name": "China",
   "population": 1431002651,
   "capital": "Beijing",
   "languages": [
      "Chinese"
   ]
}

"""

json_str_2 = """
{
    "name": "China",
    "population": "TEST",
    "capital": "Beijing",
    "languages": [
        "Chinese"
    ],"students": {
        "name": "name",
        "age":18
    }
}
"""

```

---

## DIFF JSON 

```python

d1 = json.loads(json_str)
d2 = json.loads(json_str_2)
new_result = DeepDiff(d1, d2, verbose_level=2)
print(new_result.to_json())

for key, item in new_result.items():
    print("change_type", key)
    print("change_details:")
    for element in item.values():
        print(element)
```


---

### DeepDiff 输出结果

```sh
change_type: type_changes
change_details:
root['population']:{'old_type': <class 'int'>, 'new_type': <class 'str'>, 'old_value': 1431002651, 'new_value': 'TEST'}
change_type: dictionary_item_added
change_details:
root['students']:{'name': 'name', 'age': 18}
```

如何进行封装可以自行考虑

---

### 关于操作JSON的小结

- 使用自带json的load/loads/dump/dumps
- 使用pydantic结构化和转换JSON
- 使用dotty设置不同路径的JSON值
- 使用DeepDiff比较JSON值的差异
