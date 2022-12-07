"""
Starting state
            [G] [W]         [Q]    
[Z]         [Q] [M]     [J] [F]    
[V]         [V] [S] [F] [N] [R]    
[T]         [F] [C] [H] [F] [W] [P]
[B] [L]     [L] [J] [C] [V] [D] [V]
[J] [V] [F] [N] [T] [T] [C] [Z] [W]
[G] [R] [Q] [H] [Q] [W] [Z] [G] [B]
[R] [J] [S] [Z] [R] [S] [D] [L] [J]
 1   2   3   4   5   6   7   8   9 

"""

stacks = [
    ["R", "G", "J", "B", "T", "V", "Z"],
    ["J", "R", "V", "L"],
    ["S", "Q", "F"],
    ["Z", "H", "N", "L", "F", "V", "Q", "G"],
    ["R", "Q", "T", "J", "C", "S", "M", "W"],
    ["S", "W", "T", "C", "H", "F"],
    ["D", "Z", "C", "V", "F", "N", "J"],
    ["L", "G", "Z", "D", "W", "R", "F", "Q"],
    ["J", "B", "W", "V", "P"],
]

# eg 'move 6 from 5 to 7'
def move_crates(instr):
    split_instr = instr.split()
    steps = int(split_instr[1])
    src = int(split_instr[3]) - 1
    dest = int(split_instr[5]) - 1
    for _ in range(steps):
        stacks[dest].append(stacks[src].pop())


def check_stacks():
    top_crates = ""
    for stack in stacks:
        top_crates += stack[-1]
    return top_crates


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/5/input.txt"
    with open(in_file) as f:
        for l in f:
            move_crates(l.strip())

    print(check_stacks())
