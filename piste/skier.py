#!usr/bin/python3
from math import factorial


def main(length, f):
    f = f[1:]
    list = []
    for i in f:
        i = i.replace("\n", "")
        list.append(i.split(" "))
    print(list)
    return get_lower(list, 0, length, 0)


def get_lower(list, sum, length, position):
    array = [0 for i in range(factorial(length))]
    for i in range(length):
        for ii in range(0, i + 1):
            start = ii
            end = int((i + 1)/2) + 1
            for iii in range(start, end):
                array[iii] += ii

    print(array)


if __name__ == "__main__":
    with open(input("Select file: "), "r") as file:
        f = file.readlines()
        tmp = main(int(f[0].replace("\n", "")), f)
        print(tmp)
