import csv

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'
raw_headings = "Country|Capital|CC|CC3|IAC|TimeZone|Currency"

countries_dict = {}

with open(input_filename, encoding='utf-8', newline='') as country_file:
    # country_file.readline()
    headings = raw_headings.split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in reader:
        # data = row.strip("/n").split("|")
        # country, capital, code, code3, dialing, timezone, currency = data
        # # print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")
        # country_dict = {
        #     'name': country,
        #     'capital': capital,
        #     'country_code': code,
        #     'cc3': code3,
        #     'dialing_code': dialing,
        #     'timezone': timezone,
        #     'currency': currency,
        # }
        countries_dict[row['country'].casefold()] = row
        countries_dict[row['cc'].casefold()] = row


while True:
    chosen_country = input('Enter the name of country you want to look up: ').casefold()
    if chosen_country != 'exit':
        if chosen_country in countries_dict:
            look_up = countries_dict.get(chosen_country)
            for feature in look_up:
                print(f"\t{feature}: {look_up[feature]}")
        else:
            print(f"{chosen_country} is not included in the system yet")
    else:
        break
