import json
    import urllib.request

    json_data_source = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/national/rankings/110-tavg-202204/data.json"

    # with open(json_data_source, encoding='utf-8') as data:
    with urllib.request.urlopen(json_data_source) as json_stream:
        data = json_stream.read().decode('utf-8')
        anomalies = json.loads(data)

print(anomalies['description'])

for month, month_value in anomalies['data'].items():
    value, mean = float(month_value["value"]), float(month_value["mean"])
    print(
        f"""In {month} the temperature is {value} and the average figure is {mean}""")
