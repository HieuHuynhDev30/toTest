import csv
country_file = "country_info.txt"

with open(country_file, encoding="utf-8", newline='') as country_input:
    reader = csv.DictReader(country_input, delimiter="|")
    for row in reader:
        print(row)
