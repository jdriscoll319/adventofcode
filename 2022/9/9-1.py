import numpy as np


def convert_input(inp):
    instructions = []
    with open(inp) as f:
        for l in f:
            step = l.strip().split()
            step[1] = int(step[1])
            instructions.append(step)
    return instructions


def move_hor(head, tail, seen, cnt):
    diag = head[1] - tail[1]
    head[0] += cnt
    sign = np.sign(cnt)
    for step in range(np.abs(head[0] - tail[0]) - 1):
        if diag:
            tail[1] += diag
            diag = 0
        tail[0] += sign
        seen.add(tuple(tail))
    return head, tail, seen


def move_ver(head, tail, seen, cnt):
    diag = head[0] - tail[0]
    head[1] += cnt
    sign = np.sign(cnt)
    for _ in range(np.abs(head[1] - tail[1]) - 1):
        if diag:
            tail[0] += diag
            diag = 0
        tail[1] += sign
        seen.add(tuple(tail))
    return head, tail, seen


def move_rope(instructions):
    #       x, y
    head = [0, 0]
    tail = [0, 0]
    seen = set()
    seen.add(tuple(tail))
    for dir, cnt in instructions:
        if dir == "R":
            head, tail, seen = move_hor(head, tail, seen, cnt)
        elif dir == "L":
            head, tail, seen = move_hor(head, tail, seen, -1 * cnt)
        elif dir == "U":
            head, tail, seen = move_ver(head, tail, seen, cnt)
        else:
            head, tail, seen = move_ver(head, tail, seen, -1 * cnt)

    print(len(seen))


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/9/input.txt"
    instructions = convert_input(in_file)
    move_rope(instructions)
