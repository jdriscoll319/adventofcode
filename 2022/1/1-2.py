import numpy as np

in_file = "/home/adam/projects/adventofcode/2022/1/1/input.txt"
total = 0
max = np.array([0, 0, 0])
with open(in_file, "r") as f:
    for line in f:
        if line == "\n":
            min_idx = np.argmin(max)
            if total > max[min_idx]:
                max[min_idx] = total
            total = 0
        else:
            total += int(line.strip())

print(np.sum(max))
