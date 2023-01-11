from typing import Optional

import datetime

from datetime import datetime

from pydantic import Field
from qpyone.builtins import jsontools as jt
from qpyone.core.models import BaseDataModel

from tests import TEST_BASE_PATH


def test_load():
    result = jt.load(TEST_BASE_PATH + "/example.json")
    assert isinstance(result, dict)


def test_loads():
    json_str = """
    {
  "test": "v1",
  "t2": "v2",
  "t_list": ["test","t2"],
  "t_obj": {"k1": "v1","k2": "v2"}
}
    """
    result = jt.loads(json_str)
    assert isinstance(result, dict)


def test_loads_list():
    json_str = """
    ["test","t2"]
    """
    result = jt.loads(json_str)
    assert isinstance(result, list)


class DataTransformRule(BaseDataModel):
    id: str | None = Field(None, alias="id")
    name: str | None = Field(None, alias="name")
    start_time: datetime | None = Field(None, alias="startTime")
    end_time: datetime | None = Field(None, alias="endTime")


def test_model():
    result = DataTransformRule(
        id="test", name="test", start_time=datetime.now().astimezone()
    )
    # "2032-04-23T10:20:30.400+02:30"
    print(datetime.now().astimezone())
    print(result.to_json())
    json_str = """
    {"id": "test", "name": "test", "startTime": "2022-10-24 16:04:47.657599+08:00"}
    """
    result_1 = DataTransformRule.parse_raw(result.to_json())
    print(result_1.to_json())
    print(result_1.start_time.astimezone())
