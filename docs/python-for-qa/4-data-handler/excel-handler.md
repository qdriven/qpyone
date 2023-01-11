# Python处理EXCEL

目前日常工作中常用的EXCEl场景是:
1. 接口测试数据用EXCEl保存，进行批量处理
2. 数据库数据的导出，保存到数据库
3. EXCEL实际情况和CSV类似,EXCEL基本可以和CSV一并处理

结合pydantic的处理数据，处理EXCEl会变的非常容易，通过实际例子来介绍EXCEl的用法，
会让对EXCEL处理会更加的清晰.对于测试同学来说，不需要从头开始写处理excel的程序，只需要解决工具
解决就可以.

下面介绍通过第三方依赖来解决日常工作中常见的EXCEL处理方式。


## 读取EXCEL，并转化成Python 类
![img.png](excel.png)

```python
class UnitExcelModel(BaseDataModel):
    unit_group_name: str = Field("", alias="单位组名称")
    unit_name: str = Field("", alias="单位名")
```

```python
def test_load_objects_from_excel():
    result = exceltools.read_as_objects("./unit.xlsx",
                                        UnitExcelModel)
    print(result)
    print(type(result))
```

## 写入EXCEL

```python
def test_write_excels():
    u = UnitExcelModel()
    u.unit_name = "质量"
    u.unit_group_name = "kg"
    u1 = UnitExcelModel(unit_name="test1", unit_group_name="group1")
    list_objects = [u,u1]
    exceltools.write_objects_to_excel(list_objects,"unit_demo.xlsx")
```
