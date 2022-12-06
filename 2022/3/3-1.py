import string


def inspect(items):
    comp_1 = set(items[0 : int(len(items) / 2)])
    comp_2 = set(items[int(len(items) / 2) :])
    inter = comp_1.intersection(comp_2)
    return string.ascii_letters.index(inter.pop()) + 1


def check_bags(inp):
    total = 0
    with open(inp) as f:
        for l in f:
            total += inspect(l.strip())
    return total


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/3/input.txt"
    print(check_bags(in_file))
