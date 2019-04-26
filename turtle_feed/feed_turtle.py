#!usr/bin/python3


def main(days, pamlsky):
    assert int(days) < 1000000 and len(pamlsky) < 1000000, "Too many days or pomlskek"
    types = []
    pamlsky = pamlsky.split(" ")
    for pamlsek in pamlsky:
        if pamlsek not in types:
            types += pamlsek
    for i in range(ord(min(types)), ord(max(types))):
        if chr(i) not in types:
            types += chr(i)
    types.sort()
    seznam = {}
    for type in types:
        seznam[type] = 0
    for pamlsek in pamlsky:
        seznam[pamlsek] += 1
    return seznam


def print_amount(list):
    for key in list:
        print("{}:{}".format(key, list[key]*"*"))


if __name__ == "__main__":
    with open(input("Select file: "), "r") as file:
        f = file.readlines()
        tmp = main(f[0].replace("\n", ""), f[1].replace("\n", ""))
        print_amount(tmp)
