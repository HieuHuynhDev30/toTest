import csv

csv_filename = "OlympicMedals_2020.csv"

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file)
    header = csv_file.readline().strip('\n').split(',')
    print(f'Colum header: {header}')
    for row in reader:
        rank = int(row[0])
        nation = row[1]
        print(f'{nation} was ranked {rank} in Olympic Tokyo 2020')
