"""
combine jmespath,jsonpath and dictor
- https://github.com/jmespath/jmespath.py
"""
import json
from typing import Optional, Any, Dict, Union, List

from pydantic import BaseModel


def get(key: str) -> Optional[Any]:
    pass


def set_value(target: Any, key: str, value: Any) -> Any:
    pass


def differ():
    pass


def loads(json_str: str, **kwargs):
    """
    load json str to json
    """
    return json.loads(json_str, **kwargs)


def load(file_path: str, **kwargs):
    """
    read json file to dict
    """
    with open(file_path, 'r') as f:
        return json.load(f, **kwargs)


def dumps(obj: Union[Dict,List], **kwargs)->str:
    """
    dump string as json string
    """
    return json.dumps(obj=obj, **kwargs)

class WithToJson(BaseModel):
    pass
