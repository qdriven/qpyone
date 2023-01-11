"""Tests for hello function."""
from pydantic import Field
from qpyone.builtins import exceltools
from qpyone.core.models import BaseDataModel


class UnitExcelModel(BaseDataModel):
    unit_group_name: str = Field("", alias="单位组名称")
    unit_name: str = Field("", alias="单位名")


def test_load_objects_from_excel():
    result = exceltools.read_as_objects("./unit.xlsx", UnitExcelModel)
    print(result)
    print(type(result))


def test_write_excels():
    u = UnitExcelModel()
    u.unit_name = "质量"
    u.unit_group_name = "kg"
    u1 = UnitExcelModel(unit_name="test1", unit_group_name="group1")
    list_objects = [u, u1]
    exceltools.write_objects_to_excel(list_objects, "unit_demo.xlsx")
    exceltools.write_objects_to_excel(list_objects, "unit_demo.csv")
