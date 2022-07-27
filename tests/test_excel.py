"""Tests for hello function."""
import pytest

from cewpyutils.excel import XlsxModel, XlsxField


class UnitExcelModel(XlsxModel):
    unit_group_name: str = XlsxField("", alias="单位组名称")
    unit_name: str = XlsxField("", alias="单位名")
    unit_symbol: str = XlsxField("", alias="单位符号")
    unit_latex: str = XlsxField("", alias="单位符号LaTex")
    base_unit: bool = XlsxField("", alias="基准单位")
    factor: str = XlsxField("", alias="换算系数")


def test_load_objects_from_excel():
    result = UnitExcelModel.from_file("./unit.xlsx")
    print(result)
