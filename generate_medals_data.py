import csv

key_list = "Rank,Country,Gold,Silver,Bronze,Total".split(",")
file_source = "OlympicMedals_2020.csv"
file_target = "medal_dict.py"
with open(file_source, encoding="utf-8", newline='') as input_file,\
        open(file_target, "w", encoding="utf-8") as out_file:
    reader = csv.DictReader(input_file, delimiter=",")
    print("import csv", file=out_file)
    print(file=out_file)
    print("medal_dict = [", file=out_file)
    for row in reader:
        medal_list = {}
        for key in key_list:
            value = row[key]
            if value.isnumeric():
                value = int(value)
            medal_list[key.casefold()] = value
        print(f"     {medal_list},", file=out_file)
    print("]", file=out_file)
