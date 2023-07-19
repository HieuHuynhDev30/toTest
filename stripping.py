filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "'Twasbril"
no_apostrophe = first.strip(chars)
print(no_apostrophe)
print()
twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removed = first.removesuffix("toves")
print(toves_removed)

string = "Hello World"
print(string[:-1])


def deleteprefix(text: str, prefix: str) -> str:
    """
    Delete the prefix of a given string if the string starts with the given prefix

    :param text: The string passed to the function
    :param prefix: The prefix to check if it is what `text` begins with
    :return: A string without `prefix` or the original `text`
    """
    if text.startswith(prefix):
        return text[len(prefix):]
    else:
        return text[:]


def deletesuffix(text: str, suffix: str) -> str:
    """
    Delete the suffix of a given string if the string ends with the given suffix

    :param text: The string passed to the function
    :param suffix: The suffix to check if it is what `text` ends with
    :return: A string without `suffix` or the original `text`
    """
    if suffix and text.endswith(suffix):
        return text[:-len(suffix)]
    else:
        return text[:]


print(deleteprefix("Hello World", "Hello"))
print(deletesuffix("Hello World", "World"))