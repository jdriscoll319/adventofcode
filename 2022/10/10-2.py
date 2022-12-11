def convert_input(inp):
    instructions = []
    with open(inp) as f:
        for l in f:
            step = l.strip().split()
            instructions.append(step)
    return instructions


def draw(line, px_center):
    if len(line) >= px_center - 1 and len(line) <= px_center + 1:
        line += "#"
    else:
        line += "."
    return line


def read_register(instructions):
    target = 0
    current_val = 1
    current_cycle = 1
    screen = ""
    line = ""
    for cmd in instructions:
        if cmd[0] == "noop":
            inc = 1
            val = 0
        else:
            inc = 2
            val = int(cmd[1])
        for i in range(inc):
            line = draw(line, current_val)
            current_cycle += 1
            if current_cycle > 40:
                current_cycle = 1
                screen += line + "\n"
                line = ""
        current_val += val
    print(screen)


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/10/input.txt"
    instructions = convert_input(in_file)
    read_register(instructions)
