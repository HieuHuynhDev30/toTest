jabber = open('Jabberwocky.txt', encoding='UTF-16BE')
for line in jabber:
    print(line, end='')

jabber.close()

# with open('Jabberwocky.txt', 'r') as jabber:
#     # for line in jabber:
#     #     print(line .rstrip())
#     lines = jabber.readlines()
#
#     print(lines)
#     print(lines[-1])
#     for line in reversed(lines):
#         print(line, end="")

# with open('Jabberwocky.txt') as jabber:
#     # while True:
#     #     line = jabber.readline().rstrip()
#     #     print(line)
#     #     if 'jubjub' in line.casefold():
#     #         break
#     # for line in jabber:
#     #     print(line.rstrip())
#     #     if 'jubjub' in line.casefold():
#     #         break
#     line = jabber.readline().rstrip()
#     lines = jabber.readline().rstrip()
#     print(line)
#     print(lines)
