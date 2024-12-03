VAR = "11"
CSV_PATH = "lab_3/11.csv"
JSON_PATH = "lab_3/result.json"

REGULARS = {
    "email": r"^[\w\.-]+@[\w\.-]+\.\w+$",
    "height": r"^[1-2]\.\d{2}$",
    "snils": r"^\d{11}$",
    "passport": r"^\d{2}\s\d{2}\s\d{6}$",
    "occupation": r"^[a-zA-Zа-яА-ЯёЁ\s-]+",
    "longitude": r"^-?(?:180|\d{1,2}|1[0-7]\d)(\.\d+)?$",
    "hex_color": r"^#([A-Fa-f0-9]{6})$",
    "issn": r"^\d{4}-\d{4}$",
    "locale_code": r"^[a-z]{2}(-[a-z]{2})?$",
    "time": r"^\d{2}:\d{2}:\d{2}\.\d{1,}$"
}
