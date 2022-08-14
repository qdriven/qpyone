from fluentqpy.builtins import jsontools as jt


def test_load():
    result = jt.load("./example.json")
    assert isinstance(result,dict)


def test_loads():
    json_str="""
    {
  "test": "v1",
  "t2": "v2",
  "t_list": ["test","t2"],
  "t_obj": {"k1": "v1","k2": "v2"}
}
    """
    result = jt.loads(json_str)
    assert isinstance(result,dict)

def  test_loads_list():
    json_str = """
    ["test","t2"]
    """
    result = jt.loads(json_str)
    assert isinstance(result,list)
