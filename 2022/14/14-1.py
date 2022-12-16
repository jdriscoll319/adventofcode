import numpy as np


def check_corners(coord, corners):
    corners[0] = min(corners[0], coord[0])
    corners[1] = max(corners[1], coord[0])
    corners[3] = max(corners[3], coord[1])
    return corners


def add_range(c1, c2, blocked, corners):
    c1 = tuple([int(i) for i in c1.split(",")])
    blocked.add(c1)
    corners = check_corners(c1, corners)
    c2 = tuple([int(i) for i in c2.split(",")])
    corners = check_corners(c2, corners)
    blocked.add(c2)
    for i in range(min(c1[0], c2[0]), max(c1[0], c2[0])):
        blocked.add((i, c1[1]))
        corners = check_corners((i, c1[1]), corners)
    for i in range(min(c1[1], c2[1]), max(c1[1], c2[1])):
        blocked.add((c1[0], i))
        corners = check_corners((c1[0], i), corners)

    return blocked, corners


def parse(inp):
    blocked = set()
    #          min_x, max_x, min_y, max_y
    corners = [float("inf"), 0, 0, 0]
    with open(inp) as f:
        for l in f:
            l = l.strip().split(" -> ")
            for i in range(len(l) - 1):
                blocked, corners = add_range(l[i], l[i + 1], blocked, corners)
    return blocked, corners


def check_bounds(coord, corners):
    return coord[0] < corners[0] or coord[0] > corners[1] or coord[1] > corners[3]


def count_sand(blocked, corners):
    sand = 0
    out_of_bounds = False
    while not out_of_bounds:
        cur_pos = np.array([500, 0])
        while True:
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
            out_of_bounds = check_bounds(cur_pos, corners)
            if out_of_bounds:
                break
    print(sand)


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/14/input.txt"
    blocked, corners = parse(in_file)
    count_sand(blocked, corners)
