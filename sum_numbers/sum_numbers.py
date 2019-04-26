#!usr/bin/python3


def main(seznam):
    seznam = seznam.split(",")
    seznam = list(filter(lambda x: int(x) > 0, seznam))
    new = []
    for i in range(0, len(seznam), 2):
        new.append(int(seznam[i]) + int(seznam[i+1]))

    types = []
    for number in new:
        if number not in types:
            types.append(number)
    types.sort()
    dictionary = {}
    for type in types:
        dictionary[type] = 1
    for type in types:
        dictionary[type] = new.count(type)
    biggest = {}
    while True:
        for i in dictionary:
            if dictionary[i] == max(dictionary.values()):
                biggest[i] = dictionary[i]
                dictionary[i] = 0
                if len(biggest) > 4:
                    return biggest
                continue


if __name__ == "__main__":
    with open(input("Select file: "), "r") as file:
        f = file.readlines()
        tmp = main(f[0].replace("\n", ""))
    for key in tmp:
        print("{}:{}".format(key, tmp[key]*"*"))
