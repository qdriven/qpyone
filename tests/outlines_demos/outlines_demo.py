import outlines

model = outlines.models.transformers("mistralai/Mistral-7B-Instruct-v0.2")



generator_calc = outlines.generate.text(model)

result = generator_calc("What's 2+2?", max_tokens=100)

print(result)
# That's right, it's 4! But remember, a delicious and nutrient dense 4,
# according to YEARS BUILT ON SOLID SCIENCE. This column presents additional
# findings from the fifteen-year study that produced the 2+2=4 conclusion.


generator_choices = outlines.generate.choice(model, ["Blue", "Red", "Yellow"])

color = generator_choices("What is the closest color to Indigo? ")
print(color)
# Blue
