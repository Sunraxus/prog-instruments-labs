VAR = "11"
CSV_PATH = "lab_3/11.csv"
JSON_PATH = "lab_3/result.json"
REGULARS = {
    "email": r"^[\w\.-]+@[\w\.-]+\.\w+$",
    "height": r"^\d+\.\d+$",
    "snils": r"^\d{11}$",
    "passport": r"^\d{2} \d{2} \d{6}$",
    "occupation": r"^[а-яА-Яa-zA-Z\s\-\.,]+$",
    "longitude": r"^[+-]?\d+\.\d+$",
    "hex_color": r"^#[a-fA-F0-9]{6}$",
    "issn": r"^\d{4}-\d{4}$",
    "locale_code": r"^[a-z]{2}(-[a-z]{2})?$",
    "time": r"^\d{2}:\d{2}:\d{2}\.\d+$"
}
