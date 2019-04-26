#!usr/bin/python3


def main(length, commands):
    assert len(commands) <= 1000000, "There are too many commands"
    x, y = 0, 0
    for i in range(int(length)):
        if commands[i] == "S":
            y += 1
        elif commands[i] == "J":
            y -= 1
        elif commands[i] == "V":
            x += 1
        elif commands[i] == "Z":
            x -= 1
    return x, y


if __name__ == "__main__":
    with open(input("Select file: "), "r") as file:
        f = file.readlines()
        tmp = main(f[0].replace("\n", ""), f[1].replace("\n", ""))
        print("Zelva position is {} {}".format(tmp[0], tmp[1]))
