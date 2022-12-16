import numpy as np


def add_range(c1, c2, blocked, max_y):
    c1 = tuple([int(i) for i in c1.split(",")])
    blocked.add(c1)
    max_y = max(max_y, c1[1])
    c2 = tuple([int(i) for i in c2.split(",")])
    max_y = max(max_y, c1[1])
    blocked.add(c2)
    for i in range(min(c1[0], c2[0]), max(c1[0], c2[0])):
        blocked.add((i, c1[1]))
    for i in range(min(c1[1], c2[1]), max(c1[1], c2[1])):
        blocked.add((c1[0], i))
        max_y = max(max_y, i)

    return blocked, max_y


def parse(inp):
    blocked = set()
    max_y = 0
    with open(inp) as f:
        for l in f:
            l = l.strip().split(" -> ")
            for i in range(len(l) - 1):
                blocked, max_y = add_range(l[i], l[i + 1], blocked, max_y)
    return blocked, max_y


def count_sand(blocked, max_y):
    sand = 0
    cur_pos = np.array([0, 0])
    while not np.all(cur_pos == [500, 0]):
        cur_pos = np.array([500, 0])
        while True:
            if cur_pos[1] + 1 == max_y:
                blocked.add(tuple(cur_pos))
                sand += 1
                break
            if tuple(cur_pos + [0, 1]) not in blocked:
                cur_pos += [0, 1]
            elif tuple(cur_pos + [-1, 1]) not in blocked:
                cur_pos += [-1, 1]
            elif tuple(cur_pos + [1, 1]) not in blocked:
                cur_pos += [1, 1]
            else:
                blocked.add(tuple(cur_pos))
                sand += 1
                break
    print(sand)


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/14/input.txt"
    blocked, max_y = parse(in_file)
    count_sand(blocked, max_y + 2)
