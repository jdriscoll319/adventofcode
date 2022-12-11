def convert_input(inp):
    instructions = []
    with open(inp) as f:
        for l in f:
            step = l.strip().split()
            instructions.append(step)
    return instructions


def read_register(instructions):
    sum = 0
    target = 0
    current_val = 1
    current_step = 1
    for cmd in instructions:
        if cmd[0] == "noop":
            inc = 1
            val = 0
        else:
            inc = 2
            val = int(cmd[1])
        if current_step + inc > 20 + 40 * target:
            sum += current_val * (20 + 40 * target)
            target += 1
        current_val += val
        current_step += inc
    print(sum)


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/10/input.txt"
    instructions = convert_input(in_file)
    read_register(instructions)
