import numpy as np


def convert_input(inp):
    instructions = []
    with open(inp) as f:
        for l in f:
            step = l.strip().split()
            step[1] = int(step[1])
            instructions.append(step)
    return instructions


def not_touching(k1, k2):
    return np.any(np.abs(k1 - k2) > 1)


def resolve_chain(rope, seen):
    for i in range(1, 10):
        if not_touching(rope[i - 1], rope[i]):
            rope[i] += np.sign(rope[i - 1] - rope[i])
    seen.add(tuple(rope[-1]))
    return seen


def move_rope(instructions):
    #       x, y
    rope = [np.array([0, 0]) for _ in range(10)]
    seen = set()
    seen.add(tuple(rope[-1]))
    for dir, cnt in instructions:
        if dir == "R":
            step = [1, 0]
        elif dir == "L":
            step = [-1, 0]
        elif dir == "U":
            step = [0, 1]
        else:
            step = [0, -1]
        for _ in range(cnt):
            # rope, seen = move_knot(rope, 0, 1, 0, seen)
            rope[0] += step
            seen = resolve_chain(rope, seen)

    print(len(seen))


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/9/input.txt"
    instructions = convert_input(in_file)
    move_rope(instructions)
