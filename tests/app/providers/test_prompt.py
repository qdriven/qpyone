from qpyone.app.gpt4.sp.base.prompts.base import format_prompt


def test_format_prompt():
    result = format_prompt({"test":"test"})
    print(result)
