#!/usr/bin/env python

seq = """
activity_answer_id_seq
calculation_file_id_seq
calculation_id_seq
calculation_item_id_seq
emission_item_id_seq
model_id_seq
parameter_id_seq
phase_id_seq
phase_snapshot_id_seq
product_id_seq
question_id_seq
question_option_id_seq
question_result_id_seq
question_rule_id_seq
r_calculation_parameter_id_seq
report_data_quality_and_sensitivity_id_seq
report_id_seq
report_phase_statement_id_seq
report_significant_issue_id_seq
report_uncertainty_statement_id_seq
result_id_seq
task_id_seq
unit_process_id_seq
unit_process_snapshot_id_seq
"""


def generate_postgre_seqs(schema_name: str, seqs: str):
    all_seq = seqs.split("\n")
    result = []
    for item in all_seq:
        if len(item) > 1:
            result.append(generate_postgres_seq(schema_name, item))
    return result


def generate_postgres_seq(
    schema_name: str, seq_name: str, table_name: str = None
) -> str:
    temp = "select setval('{}.{}'::regclass,max(id)) from {};"
    if table_name is None:
        table_name = seq_name.replace("_id_seq", "")
    return temp.format(schema_name, seq_name, table_name)


def test_seq():
    print(seq)
    result = generate_postgre_seqs("calculator", seq)
    for item in result:
        print(item)
