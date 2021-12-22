import re
from collections import OrderedDict


def parse_notes(text: str) -> OrderedDict:
    parsed_data = re.findall(r"((?:\d+.\d+.\d{4})\n(?:\d+ - (?:.+)(?:\n|$))+)", text)

    biggest_costs = {}
    max_len_biggest_costs = 10

    data = OrderedDict()
    for item in parsed_data:
        date = re.search(r"\d+.\d+.\d{4}", item).group(0)
        arr_info = re.findall(r"(\d+) - (.+)(?:\n|$)", item)

        costs = []
        for info in arr_info:
            costs.append(
                {
                    "price": info[0],
                    "comment": info[1]
                }
            )


        data[date] = costs

    return data
