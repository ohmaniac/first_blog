import json

dog_data = {
  "name": "Frieda",
  "is_dog": True,
  "hobbies": ["eating", "sleeping", "barking",],
  "age": 8,
  "address": {
    "work": None,
    "home": ("Berlin", "Germany",),
  },
  "friends": [
    {
      "name": "Philipp",
      "hobbies": ["eating", "sleeping", "reading",],
    },
    {
      "name": "Mitch",
      "hobbies": ["running", "snacking",],
    },
  ],
}

with open("hello_frieda.json", mode="w", encoding="utf-8") as write_file:
    json.dump(dog_data, write_file, indent=4) 
    # indent sorgt dafür, dass die JSON-Datei anständig (mit Einrückung) formatiert ist.
    # Ohne indent wäre in der Datei nur ein unformatierter String am Stück.