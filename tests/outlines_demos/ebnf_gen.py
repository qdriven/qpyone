from outlines import models, generate

arithmetic_grammar = """
    ?start: sum

    ?sum: product
        | sum "+" product   -> add
        | sum "-" product   -> sub

    ?product: atom
        | product "*" atom  -> mul
        | product "/" atom  -> div

    ?atom: NUMBER           -> number
         | "-" atom         -> neg
         | "(" sum ")"

    %import common.NUMBER
    %import common.WS_INLINE

    %ignore WS_INLINE
"""

model = models.transformers("mistralai/Mistral-7B-Instruct-v0.2")
generator = generate.cfg(model, arithmetic_grammar, max_tokens=100)

result = generator("Question: How can you write 5*5 using addition?\nAnswer:")
print(result)
# 5+5+5+5+5
