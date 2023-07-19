import csv

medal_dict = [
    {'rank': 1, 'country': 'United States', 'gold': 39, 'silver': 41, 'bronze': 33, 'total': 113},
    {'rank': 2, 'country': 'China', 'gold': 38, 'silver': 32, 'bronze': 18, 'total': 88},
    {'rank': 3, 'country': 'Japan', 'gold': 27, 'silver': 14, 'bronze': 17, 'total': 58},
    {'rank': 4, 'country': 'Great Britain', 'gold': 22, 'silver': 21, 'bronze': 22, 'total': 65},
    {'rank': 5, 'country': 'ROC', 'gold': 20, 'silver': 28, 'bronze': 23, 'total': 71},
    {'rank': 6, 'country': 'Australia', 'gold': 17, 'silver': 7, 'bronze': 22, 'total': 46},
    {'rank': 7, 'country': 'Netherlands', 'gold': 10, 'silver': 12, 'bronze': 14, 'total': 36},
    {'rank': 8, 'country': 'France', 'gold': 10, 'silver': 12, 'bronze': 11, 'total': 33},
    {'rank': 9, 'country': 'Germany', 'gold': 10, 'silver': 11, 'bronze': 16, 'total': 37},
    {'rank': 10, 'country': 'Italy', 'gold': 10, 'silver': 10, 'bronze': 20, 'total': 40},
    {'rank': 11, 'country': 'Canada', 'gold': 7, 'silver': 6, 'bronze': 11, 'total': 24},
    {'rank': 12, 'country': 'Brazil', 'gold': 7, 'silver': 6, 'bronze': 8, 'total': 21},
    {'rank': 13, 'country': 'New Zealand', 'gold': 7, 'silver': 6, 'bronze': 7, 'total': 20},
    {'rank': 14, 'country': 'Cuba', 'gold': 7, 'silver': 3, 'bronze': 5, 'total': 15},
    {'rank': 15, 'country': 'Hungary', 'gold': 6, 'silver': 7, 'bronze': 7, 'total': 20},
    {'rank': 16, 'country': 'South Korea', 'gold': 6, 'silver': 4, 'bronze': 10, 'total': 20},
    {'rank': 17, 'country': 'Poland', 'gold': 4, 'silver': 5, 'bronze': 5, 'total': 14},
    {'rank': 18, 'country': 'Czech Republic', 'gold': 4, 'silver': 4, 'bronze': 3, 'total': 11},
    {'rank': 19, 'country': 'Kenya', 'gold': 4, 'silver': 4, 'bronze': 2, 'total': 10},
    {'rank': 20, 'country': 'Norway', 'gold': 4, 'silver': 2, 'bronze': 2, 'total': 8},
    {'rank': 21, 'country': 'Jamaica', 'gold': 4, 'silver': 1, 'bronze': 4, 'total': 9},
    {'rank': 22, 'country': 'Spain', 'gold': 3, 'silver': 8, 'bronze': 6, 'total': 17},
    {'rank': 23, 'country': 'Sweden', 'gold': 3, 'silver': 6, 'bronze': 0, 'total': 9},
    {'rank': 24, 'country': 'Switzerland', 'gold': 3, 'silver': 4, 'bronze': 6, 'total': 13},
    {'rank': 25, 'country': 'Denmark', 'gold': 3, 'silver': 4, 'bronze': 4, 'total': 11},
    {'rank': 26, 'country': 'Croatia', 'gold': 3, 'silver': 3, 'bronze': 2, 'total': 8},
    {'rank': 27, 'country': 'Iran', 'gold': 3, 'silver': 2, 'bronze': 2, 'total': 7},
    {'rank': 28, 'country': 'Serbia', 'gold': 3, 'silver': 1, 'bronze': 5, 'total': 9},
    {'rank': 29, 'country': 'Belgium', 'gold': 3, 'silver': 1, 'bronze': 3, 'total': 7},
    {'rank': 30, 'country': 'Bulgaria', 'gold': 3, 'silver': 1, 'bronze': 2, 'total': 6},
    {'rank': 31, 'country': 'Slovenia', 'gold': 3, 'silver': 1, 'bronze': 1, 'total': 5},
    {'rank': 32, 'country': 'Uzbekistan', 'gold': 3, 'silver': 0, 'bronze': 2, 'total': 5},
    {'rank': 33, 'country': 'Georgia', 'gold': 2, 'silver': 5, 'bronze': 1, 'total': 8},
    {'rank': 34, 'country': 'Chinese Taipei', 'gold': 2, 'silver': 4, 'bronze': 6, 'total': 12},
    {'rank': 35, 'country': 'Turkey', 'gold': 2, 'silver': 2, 'bronze': 9, 'total': 13},
    {'rank': 36, 'country': 'Greece', 'gold': 2, 'silver': 1, 'bronze': 1, 'total': 4},
    {'rank': 36, 'country': 'Uganda', 'gold': 2, 'silver': 1, 'bronze': 1, 'total': 4},
    {'rank': 38, 'country': 'Ecuador', 'gold': 2, 'silver': 1, 'bronze': 0, 'total': 3},
    {'rank': 39, 'country': 'Ireland', 'gold': 2, 'silver': 0, 'bronze': 2, 'total': 4},
    {'rank': 39, 'country': 'Israel', 'gold': 2, 'silver': 0, 'bronze': 2, 'total': 4},
    {'rank': 41, 'country': 'Qatar', 'gold': 2, 'silver': 0, 'bronze': 1, 'total': 3},
    {'rank': 42, 'country': 'Bahamas', 'gold': 2, 'silver': 0, 'bronze': 0, 'total': 2},
    {'rank': 42, 'country': 'Kosovo', 'gold': 2, 'silver': 0, 'bronze': 0, 'total': 2},
    {'rank': 44, 'country': 'Ukraine', 'gold': 1, 'silver': 6, 'bronze': 12, 'total': 19},
    {'rank': 45, 'country': 'Belarus', 'gold': 1, 'silver': 3, 'bronze': 3, 'total': 7},
    {'rank': 46, 'country': 'Romania', 'gold': 1, 'silver': 3, 'bronze': 0, 'total': 4},
    {'rank': 46, 'country': 'Venezuela', 'gold': 1, 'silver': 3, 'bronze': 0, 'total': 4},
    {'rank': 48, 'country': 'India', 'gold': 1, 'silver': 2, 'bronze': 4, 'total': 7},
    {'rank': 49, 'country': 'Hong Kong', 'gold': 1, 'silver': 2, 'bronze': 3, 'total': 6},
    {'rank': 50, 'country': 'Philippines', 'gold': 1, 'silver': 2, 'bronze': 1, 'total': 4},
    {'rank': 50, 'country': 'Slovakia', 'gold': 1, 'silver': 2, 'bronze': 1, 'total': 4},
    {'rank': 52, 'country': 'South Africa', 'gold': 1, 'silver': 2, 'bronze': 0, 'total': 3},
    {'rank': 53, 'country': 'Austria', 'gold': 1, 'silver': 1, 'bronze': 5, 'total': 7},
    {'rank': 54, 'country': 'Egypt', 'gold': 1, 'silver': 1, 'bronze': 4, 'total': 6},
    {'rank': 55, 'country': 'Indonesia', 'gold': 1, 'silver': 1, 'bronze': 3, 'total': 5},
    {'rank': 56, 'country': 'Ethiopia', 'gold': 1, 'silver': 1, 'bronze': 2, 'total': 4},
    {'rank': 56, 'country': 'Portugal', 'gold': 1, 'silver': 1, 'bronze': 2, 'total': 4},
    {'rank': 58, 'country': 'Tunisia', 'gold': 1, 'silver': 1, 'bronze': 0, 'total': 2},
    {'rank': 59, 'country': 'Estonia', 'gold': 1, 'silver': 0, 'bronze': 1, 'total': 2},
    {'rank': 59, 'country': 'Fiji', 'gold': 1, 'silver': 0, 'bronze': 1, 'total': 2},
    {'rank': 59, 'country': 'Latvia', 'gold': 1, 'silver': 0, 'bronze': 1, 'total': 2},
    {'rank': 59, 'country': 'Thailand', 'gold': 1, 'silver': 0, 'bronze': 1, 'total': 2},
    {'rank': 63, 'country': 'Bermuda', 'gold': 1, 'silver': 0, 'bronze': 0, 'total': 1},
    {'rank': 63, 'country': 'Morocco', 'gold': 1, 'silver': 0, 'bronze': 0, 'total': 1},
    {'rank': 63, 'country': 'Puerto Rico', 'gold': 1, 'silver': 0, 'bronze': 0, 'total': 1},
    {'rank': 66, 'country': 'Colombia', 'gold': 0, 'silver': 4, 'bronze': 1, 'total': 5},
    {'rank': 67, 'country': 'Azerbaijan', 'gold': 0, 'silver': 3, 'bronze': 4, 'total': 7},
    {'rank': 68, 'country': 'Dominican Republic', 'gold': 0, 'silver': 3, 'bronze': 2, 'total': 5},
    {'rank': 69, 'country': 'Armenia', 'gold': 0, 'silver': 2, 'bronze': 2, 'total': 4},
    {'rank': 70, 'country': 'Kyrgyzstan', 'gold': 0, 'silver': 2, 'bronze': 1, 'total': 3},
    {'rank': 71, 'country': 'Mongolia', 'gold': 0, 'silver': 1, 'bronze': 3, 'total': 4},
    {'rank': 72, 'country': 'Argentina', 'gold': 0, 'silver': 1, 'bronze': 2, 'total': 3},
    {'rank': 72, 'country': 'San Marino', 'gold': 0, 'silver': 1, 'bronze': 2, 'total': 3},
    {'rank': 74, 'country': 'Jordan', 'gold': 0, 'silver': 1, 'bronze': 1, 'total': 2},
    {'rank': 74, 'country': 'Malaysia', 'gold': 0, 'silver': 1, 'bronze': 1, 'total': 2},
    {'rank': 74, 'country': 'Nigeria', 'gold': 0, 'silver': 1, 'bronze': 1, 'total': 2},
    {'rank': 77, 'country': 'Bahrain', 'gold': 0, 'silver': 1, 'bronze': 0, 'total': 1},
    {'rank': 77, 'country': 'Saudi Arabia', 'gold': 0, 'silver': 1, 'bronze': 0, 'total': 1},
    {'rank': 77, 'country': 'Lithuania', 'gold': 0, 'silver': 1, 'bronze': 0, 'total': 1},
    {'rank': 77, 'country': 'North Macedonia', 'gold': 0, 'silver': 1, 'bronze': 0, 'total': 1},
    {'rank': 77, 'country': 'Namibia', 'gold': 0, 'silver': 1, 'bronze': 0, 'total': 1},
    {'rank': 77, 'country': 'Turkmenistan', 'gold': 0, 'silver': 1, 'bronze': 0, 'total': 1},
    {'rank': 83, 'country': 'Kazakhstan', 'gold': 0, 'silver': 0, 'bronze': 8, 'total': 8},
    {'rank': 84, 'country': 'Mexico', 'gold': 0, 'silver': 0, 'bronze': 4, 'total': 4},
    {'rank': 85, 'country': 'Finland', 'gold': 0, 'silver': 0, 'bronze': 2, 'total': 2},
    {'rank': 86, 'country': 'Botswana', 'gold': 0, 'silver': 0, 'bronze': 1, 'total': 1},
    {'rank': 86, 'country': 'Burkina Faso', 'gold': 0, 'silver': 0, 'bronze': 1, 'total': 1},
    {'rank': 86, 'country': "Côte d'Ivoire", 'gold': 0, 'silver': 0, 'bronze': 1, 'total': 1},
    {'rank': 86, 'country': 'Ghana', 'gold': 0, 'silver': 0, 'bronze': 1, 'total': 1},
    {'rank': 86, 'country': 'Grenada', 'gold': 0, 'silver': 0, 'bronze': 1, 'total': 1},
    {'rank': 86, 'country': 'Kuwait', 'gold': 0, 'silver': 0, 'bronze': 1, 'total': 1},
    {'rank': 86, 'country': 'Moldova', 'gold': 0, 'silver': 0, 'bronze': 1, 'total': 1},
    {'rank': 86, 'country': 'Syria', 'gold': 0, 'silver': 0, 'bronze': 1, 'total': 1},
]

columns = ['rank', 'country', 'gold', 'silver', 'bronze']

filename = "country_medal.csv"


def country(d: dict) -> str:
    return d['country']


with open(filename, 'w', encoding='utf-8', newline='') as output_csv:
    writer = csv.DictWriter(output_csv, fieldnames=columns, delimiter="|", extrasaction='ignore')
    writer.writeheader()
    writer.writerows(sorted(medal_dict, key=country))
    # for row in medal_dict:
    #      writer.writerow(row)

list_test = [10, 45, 89, 32, 61, 72]

def mod_number(i: int) -> int:
    return i % 10

print(sorted(list_test, key=mod_number))
