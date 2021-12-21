from collections import OrderedDict

from helpers import convert_str_to_date, ceil_to_hundredth


def calculate_all_statistic(data: OrderedDict) -> dict:
    all_costs = 0

    data_items = list(data.items())

    for day, day_values in data_items:
        for purchase in day_values:
            all_costs += int(purchase['price'])

    arithmetic_mean_per_day = calculate_arithmetic_mean_per_day(all_costs, data_items[0][0], data_items[-1][0])

    return {
        "all_costs": all_costs,
        "arithmetic_mean_per_day": arithmetic_mean_per_day
    }


def calculate_arithmetic_mean_per_day(all_costs: int, first_date: str, last_date: str) -> float:
    first_date = convert_str_to_date(first_date)
    last_date = convert_str_to_date(last_date)

    timedelta = last_date - first_date
    days = timedelta.days
    arithmetic_mean_per_day = ceil_to_hundredth(all_costs / days)

    return arithmetic_mean_per_day
