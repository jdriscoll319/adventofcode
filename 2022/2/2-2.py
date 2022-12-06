"""
A - rock, 1 pt
B - paper, 2pt
C - scissor, 3pt
X - lose
Y - draw
Z - win
"""

to_points = {"R": 1, "P": 2, "S": 3}
lose = [0, {"A": "S", "B": "R", "C": "P"}]
draw = [3, {"A": "R", "B": "P", "C": "S"}]
win = [6, {"A": "P", "B": "S", "C": "R"}]
outcome = {"X": lose, "Y": draw, "Z": win}


def score(elf, strat):
    choice = outcome[strat][1][elf]
    return outcome[strat][0] + to_points[choice]


def rps(inp):
    final_score = 0
    with open(inp) as f:
        for line in f:
            final_score += score(line[0], line[2])

    return final_score


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/2/input.txt"
    print(rps(in_file))
