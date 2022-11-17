from typing import Optional

import datetime

from pydantic import BaseModel
from pydantic import ValidationError
from pydantic import validator


class UserHistory(BaseModel):
    runid: float
    job_id: float | None
    id: str | None
    user: str | None
    status: str | None
    event_time: datetime.datetime = datetime.datetime.now()
    comment: str

    @validator("comment")
    def comment_must_contain_comment(cls, v):
        if "t" not in v:
            raise ValueError("must contain a t")
        return v.title()


def test_dict_to_model():
    external_data = {
        "runid": 1.234,
        "id": "123",
        "event_time": "2019-06-01 12:22",
        "user": "user",
        "comment": "test",
    }
    try:
        user = UserHistory(**external_data)
        assert user.id == "123"
        print(user.json())
        print(user.dict())
    except ValidationError as e:
        print(e.json())


def test_json_to_model():
    jsonstr = """
{"runid": 1.234, "job_id": null, "id": "123", "user": "user", "status": null, "event_time": "2019-06-01T12:22:00", "comment": "Test"}
    """
    user = UserHistory.parse_raw(jsonstr)
    assert user.id == "123"


class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    @validator("name")
    def name_must_contain_space(cls, v):
        if " " not in v:
            raise ValueError("must contain a space")
        return v.title()

    @validator("password2")
    def passwords_match(cls, v, values, **kwargs):
        if "password1" in values and v != values["password1"]:
            raise ValueError("passwords do not match")
        return v

    @validator("username")
    def username_alphanumeric(cls, v):
        assert v.isalnum(), "must be alphanumeric"
        return v


user = UserModel(
    name="samuel colvin",
    username="scolvin",
    password1="zxcvbn",
    password2="zxcvbn",
)
print(user)


# > name='Samuel Colvin' username='scolvin' password1='zxcvbn' password2='zxcvbn'


def test_validation():
    try:
        UserModel(
            name="samuel",
            # username='scolvin',
            password1="zxcvbn",
            password2="zxcvbn2",
        )
    except ValidationError as e:
        print(e)
        print(e.json())
        """
        2 validation errors for UserModel
        name
          must contain a space (type=value_error)
        password2
          passwords do not match (type=value_error)
        """
