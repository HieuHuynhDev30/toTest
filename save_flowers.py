data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_filename = "flower_print.txt"
#
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         print(plant, file=plants)
#
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
#
#
# print(new_list)

plants_filename = "flower_write.txt"

with open(plants_filename, "w") as plants:
    for plant in data:
        plants.write(plant)

print(type(data.__str__()))

filename = "test_numbers.txt"
with open(filename, "w") as test:
    for i in range(20):
        test.write(str(i) + '\n')
    # for i in range(20):
    #     print(i, file=test)