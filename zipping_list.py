import csv
albums = (("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          )

keys = ['album', 'artist', 'year']
filename = 'albumsV2.csv'
with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys, delimiter='|')
    writer.writeheader()
    for row in albums:
        zip_object = zip(keys, row)
        album_dict = dict(zip_object)
        print(album_dict)
        writer.writerow(album_dict)
        # for item in zip_object:
        #     print(item)