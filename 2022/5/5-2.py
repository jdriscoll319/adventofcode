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
    "RGJBTVZ",
    "JRVL",
    "SQF",
    "ZHNLFVQG",
    "RQTJCSMW",
    "SWTCHF",
    "DZCVFNJ",
    "LGZDWRFQ",
    "JBWVP",
]

# eg 'move 6 from 5 to 7'
def move_crates(instr):
    split_instr = instr.split()
    steps = int(split_instr[1])
    src = int(split_instr[3]) - 1
    dest = int(split_instr[5]) - 1
    stacks[dest] += stacks[src][-steps:]
    stacks[src] = stacks[src][:-steps]


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
