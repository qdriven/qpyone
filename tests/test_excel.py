"""Tests for hello function."""

from qpyone.misc.excel import FXlsxField
from qpyone.misc.excel import XlsxModel

from tests import TEST_BASE_PATH


class UnitExcelModel(XlsxModel):
    unit_group_name: str = FXlsxField("", alias="单位组名称")
    unit_name: str = FXlsxField("", alias="单位名")


def test_load_objects_from_excel():
    result = UnitExcelModel.from_file(TEST_BASE_PATH + "unit.xlsx")
    print(result)
