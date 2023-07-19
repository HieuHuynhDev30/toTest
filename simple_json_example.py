import json

languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]
with open('text.json', 'w', encoding='utf-8') as textfile:
    json.dump(languages, textfile)

with open('text.json', 'r', encoding='utf-8') as textfile:
    data = json.load(textfile)

print(data[5])