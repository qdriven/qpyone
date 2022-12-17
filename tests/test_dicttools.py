more_json_dict = """
{
  "characters": {
    "Lonestar": {
      "id": 55923,
      "role": "renegade",
      "items": ["space winnebago", "leather jacket"]
    },
    "Barfolomew": {
      "id": 55924,
      "role": "mawg",
      "items": ["peanut butter jar", "waggy tail"]
    },
    "Dark Helmet": {
      "id": 99999,
      "role": "Good is dumb",
      "items": ["Shwartz", "helmet"]
    },
    "Skroob": {
      "id": 12345,
      "role": "Spaceballs CEO",
      "items": ["luggage"]
    }
  }
}
"""


more_dict = {
    "characters": {
        "Lonestar": {
            "id": 55923,
            "role": "renegade",
            "items": ["space winnebago", "leather jacket"],
        },
        "Barfolomew": {
            "id": 55924,
            "role": "mawg",
            "items": ["peanut butter jar", "waggy tail"],
        },
        "Dark Helmet": {
            "id": 99999,
            "role": "Good is dumb",
            "items": ["Shwartz", "helmet"],
        },
        "Skroob": {"id": 12345, "role": "Spaceballs CEO", "items": ["luggage"]},
    }
}

from qpyone.builtins import dicttools as dt
from qpyone.builtins import jsontools as jt


def test_dict_json():

    print(dt.dict_json(jt.loads(more_json_dict), path="characters"))
