# pydantic-model

pydantic 主要作用:
1. 强制使用python的类型，可以让程序更加的方便维护
2. 提供了字段强大和开发的字段检查功能
3. 内置了json/dict和对象的转换功能

## pydantic 使用 - model类定义

每一个类的成员变量都提供了类型
```python
class CategoryApi(BaseDataModel):
    id: Optional[str] = Field(None,alias="id")
    name: Optional[str] = Field(None,alias="name")
    description: Optional[str] = Field(None,alias="description")
    status: Optional[StatusApi] = Field(None,alias="status")
    creator: Optional[str] = Field(None,alias="creator")
    parent_id: Optional[str] = Field(None,alias="parentId")
    created_time: Optional[str] = Field(None,alias="createdTime")
    updated_time: Optional[str] = Field(None,alias="updatedTime")
    archive_time: Optional[str] = Field(None,alias="archiveTime")
    childs: Optional[List[CategoryApi]] = Field(None,alias="childs")
    parents: Optional[List[CategoryApi]] = Field(None,alias="parents")

```

## pydantic 字段检查

运行后直接会报错:
```shell
[
  {
    "loc": [
      "comment"
    ],
    "msg": "must contain a comment",
    "type": "value_error"
  }
]

```
```python
class UserHistory(BaseModel):
    runid: float
    job_id: float | None
    id: str | None
    user: str | None
    status: str | None
    event_time: datetime.datetime = datetime.datetime.now()
    comment: str

    @validator('comment')
    def comment_must_contain_comment(cls, v):
        if 'comment' not in v:
            raise ValueError('must contain a comment')
        return v.title()


def test_dict_to_model():
    external_data = {
        "runid": 1.234,
        'id': '123',
        'event_time': '2019-06-01 12:22',
        'user': "user",
        "comment": "test"
    }
    try:
        user = UserHistory(**external_data)
        assert user.id == "123"
    except ValidationError as e:
        print(e.json())

```

## json/dict 通过pydantic定义的类转换

- dict 直接变成python的类:

```python
 external_data = {
        "runid": 1.234,
        'id': '123',
        'event_time': '2019-06-01 12:22',
        'user': "user",
        "comment": "test"
    }
user = UserHistory(**external_data)
```

- json直接转换成python的类

```python
    jsonstr = """
{"runid": 1.234, "job_id": null, "id": "123", "user": "user", "status": null, "event_time": "2019-06-01T12:22:00", "comment": "Test"}
    """
    user = UserHistory.parse_raw(jsonstr)
    assert user.id =="123"
```

- python类之间转json/dict

```python
    external_data = {
        "runid": 1.234,
        'id': '123',
        'event_time': '2019-06-01 12:22',
        'user': "user",
        "comment": "test"
    }
    try:
        user = UserHistory(**external_data)
        assert user.id == "123"
        print(user.json())
        print(user.dict())
    except ValidationError as e:
        print(e.json())
```

- save or update
