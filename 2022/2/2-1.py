"""
A, X - rock, 1 pt
B, Y - paper, 2pt
C, Z - scissor, 3pt
"""
to_points = {"X": 1, "Y": 2, "Z": 3}
elf_to_me = {"A": "Z", "B": "X", "C": "Y"}
me_to_elf = {"X": "C", "Y": "A", "Z": "B"}


def score(elf, me):
    if me_to_elf[me] == elf:
        return 6 + to_points[me]

    if elf_to_me[elf] == me:
        return 0 + to_points[me]

    return 3 + to_points[me]


def rps(inp):
    final_score = 0
    with open(inp) as f:
        for line in f:
            final_score += score(line[0], line[2])

    return final_score


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/2/input.txt"
    print(rps(in_file))
