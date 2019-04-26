#!usr/bin/python3


def main(data):
    row = data[0].replace("\n", "")
    capacity = row.split(" ")[0]
    bus = 1
    count = 0

    data = data[1:]
    for i in data:
        temp = int(i.replace("\n", ""))
        if count + temp > int(capacity):
            bus += 1
            count = 0
        count += temp

    return bus


with open(input("Select file: "), "r") as file:
    f = file.readlines()
    tmp = main(f)
    print("number of buses : %s" % tmp)
