from datetime import datetime
from math import ceil


def ceil_to_hundredth(number: float) -> float:
    return ceil(number * 100) / 100.0


def convert_str_to_date(string: str) -> datetime:
    return datetime.strptime(string, '%d.%m.%Y')
