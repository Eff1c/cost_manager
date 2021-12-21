from parser import parse_notes
from statistic import calculate_all_statistic


with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()

data = parse_notes(text)
statistic_dict = calculate_all_statistic(data)

print(statistic_dict)
