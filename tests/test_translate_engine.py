#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os.path

from fsdk.dltranslator.translate_engine import Translater

BASE_PATH = os.path.dirname(__file__).replace("/tests", "")
print(BASE_PATH)
source_prefix = "../docs/ecoinvent/en/data-quality"
target_prefix = "../docs/ecoinvent/cn/data-quality"
file_name = "6. Completeness.md"
file_list = ["7-Good-Practice-Documentation.md",
             "8.language.md", "9.naming-conventions.md",
             "10.default-values-basic-uncentainty.md", "11.special-condition.md",
             "12.validation-review.md", "13.embedding-new-dataset.md"]


def test_translate():
    for file_md_name in file_list:
        print("current file is {}".format(file_md_name))
        Translater().translate(source_prefix + "/" + file_md_name,
                               target_prefix + "/" + file_md_name)
