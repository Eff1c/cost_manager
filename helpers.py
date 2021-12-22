from datetime import datetime
from math import ceil


def ceil_to_hundredth(number: float) -> float:
    return ceil(number * 100) / 100.0


def convert_str_to_date(string: str) -> datetime:
    return datetime.strptime(string, '%d.%m.%Y')


def check_to_add_to_biggest_costs(biggest_costs, max_len, key, value, date):
    items = biggest_costs.items()
    prices = map(ceil_to_hundredth, map(float, biggest_costs.keys()))

    if len(items) < max_len or value > prices:
        biggest_costs[key] = value + f"({date})"
