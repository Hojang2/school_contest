#!usr/bin/python3


def main(bug, program):

    assert len(bug) <= 200000 and len(program) <= 200000, "Program or bug are too long"
    while True:
        if bug not in program:
            break
        program = program.replace(bug, "")
    return program


if __name__ == "__main__":
    with open(input("Select file: "), "r") as file:
        f = file.readlines()
        tmp = main(f[0].replace("\n", ""), f[1].replace("\n", ""))
    with open("vysledek.txt", "w") as file:
        file.write(tmp)
