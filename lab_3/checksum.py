import json
import hashlib
import csv
import re
from constants import VAR, CSV_PATH, JSON_PATH, REGULARS
from typing import List

def calculate_checksum(row_numbers: List[int]) -> str:
    """
    Вычисляет MD5 хэш от списка целочисленных значений.
    :param row_numbers: Список индексов строк, содержащих ошибки валидации.
    :return: MD5 хэш в виде строки.
    """
    row_numbers.sort()
    return hashlib.md5(json.dumps(row_numbers).encode('utf-8')).hexdigest()

def serialize_result(variant: str, checksum: str) -> None:
    """
    Сериализует результат проверки в JSON-файл.
    :param variant: Номер варианта лабораторной работы.
    :param checksum: Вычисленная контрольная сумма.
    """
    result = {
        "variant": variant,
        "checksum": checksum
    }
    with open(JSON_PATH, 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4)

def read_csv(file_path: str):
    """
    Читает CSV файл и возвращает его содержимое в виде списка словарей.
    :param file_path: Путь к файлу CSV.
    :return: Список словарей, где ключи - это имена столбцов, а значения - данные строк.
    """
    data = []
    with open(file_path, 'r', encoding='utf-16') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data

def validate_data(data, regulars):
    """
    Проверяет каждую строку данных на соответствие регулярным выражениям.
    :param data: Список словарей, представляющих строки данных.
    :param regulars: Словарь регулярных выражений для проверки.
    :return: Список булевых значений, где True означает валидность строки.
    """
    validated_data = []
    for row in data:
        is_valid = True
        for key, pattern in regulars.items():
            if key in row and not re.match(pattern, row[key].strip('"')):
                is_valid = False
                break
        validated_data.append(is_valid)
    return validated_data

def get_invalid_rows(data, regulars):
    """
    Возвращает индексы строк, которые не прошли проверку.
    :param data: Список словарей, представляющих строки данных.
    :param regulars: Словарь регулярных выражений для проверки.
    :return: Список индексов невалидных строк.
    """
    validated_data = validate_data(data, regulars)
    invalid_rows = [index for index, is_valid in enumerate(validated_data) if not is_valid]
    return invalid_rows

if __name__ == "__main__":
    data = read_csv(CSV_PATH)
    invalid_indices = get_invalid_rows(data, REGULARS)
    checksum = calculate_checksum(invalid_indices)
    serialize_result(VAR, checksum)
