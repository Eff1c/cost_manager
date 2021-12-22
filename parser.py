import re
from collections import OrderedDict


def parse_notes(text: str) -> OrderedDict:
    parsed_data = re.findall(r"(\d{2}.\d{2}.\d{4}\n(?:\d+ - [\w() ]+\n)+)", text)

    data = OrderedDict()
    for item in parsed_data:
        date = re.search(r"\d{2}.\d{2}.\d{4}", item).group(0)
        arr_info = re.findall(r"(\d+) - (.+)(\n|$)", item)
        data[date] = [
            {
                "price": info[0], "comment": info[1]
            } for info in arr_info
        ]

    return data
