from enum import Enum
from pydantic import BaseModel, constr, conint

import outlines

class Armor(str, Enum):
    leather = "leather"
    chainmail = "chainmail"
    plate = "plate"


class Character(BaseModel):
    name: constr(max_length=10)
    age: conint(gt=18, lt=99)
    armor: Armor
    strength: conint(gt=1, lt=100)

model = outlines.models.transformers("mistralai/Mistral-7B-Instruct-v0.2")
generator = outlines.generate.json(model, Character)

character = generator(
    "Generate a new character for my awesome game: "
    + "name, age (between 1 and 99), armor and strength. "
    )
print(character)
# name='Orla' age=21 armor=<Armor.plate: 'plate'> strength=8
