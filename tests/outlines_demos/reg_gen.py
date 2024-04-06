from outlines import models, generate

model = models.transformers("mistralai/Mistral-7B-Instruct-v0.2")

regex_str = r"((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)"
generator = generate.regex(model, regex_str)

result = generator("What is the IP address of localhost?\nIP: ")
print(result)
# 127.0.0.100
