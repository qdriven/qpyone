"""Tests for hello function."""
import pytest

from fluentqpy.excel import XlsxModel, FXlsxField


class UnitExcelModel(XlsxModel):
    unit_group_name: str = FXlsxField("", alias="单位组名称")
    unit_name: str = FXlsxField("", alias="单位名")


def test_load_objects_from_excel():
    result = UnitExcelModel.from_file("./unit.xlsx")
    print(result)
