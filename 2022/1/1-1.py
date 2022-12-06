import numpy as np

in_file = "/home/adam/projects/adventofcode/2022/1/input.txt"
total = 0
max = 0
with open(in_file, "r") as f:
    for line in f:
        if line == "\n":
            min_idx = max
            if total > max:
                max = total
            total = 0
        else:
            total += int(line.strip())

print(max)
