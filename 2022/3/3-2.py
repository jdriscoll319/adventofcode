import string


def compare_group(group):
    bag_1 = set(group[0])
    bag_2 = set(group[1])
    bag_3 = set(group[2])
    inter = bag_1.intersection(bag_2, bag_3)
    return string.ascii_letters.index(inter.pop()) + 1


def check_groups(inp):
    total = 0
    group = [None] * 3
    with open(inp) as f:
        for i, l in enumerate(f):
            if i > 0 and i % 3 == 0:
                total += compare_group(group)
            group[i % 3] = l.strip()
        total += compare_group(group)
    return total


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/3/input.txt"
    print(check_groups(in_file))
