def check_pair(pair):
    first_start = int(pair[: pair.find("-")])
    first_end = int(pair[pair.find("-") + 1 : pair.find(",")]) + 1
    first = set(range(first_start, first_end))
    comma = pair.find(",")
    second_start = int(pair[comma + 1 : pair.find("-", comma)])
    second_end = int(pair[pair.find("-", comma) + 1 :]) + 1
    second = set(range(second_start, second_end))
    return first.issubset(second) or first.issuperset(second)


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/4/input.txt"
    num_supersets = 0
    with open(in_file) as f:
        for l in f:
            num_supersets += check_pair(l.strip())

    print(num_supersets)
