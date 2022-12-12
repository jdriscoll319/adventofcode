from typing import Callable


class Monkey:
    def __init__(self, name) -> None:
        self.name = name
        self.items: list[int] = []
        self.friends: dict[int, Monkey] = {}
        self.operation: Callable[[int], int] = None
        self.operator: str = None
        self.operation_term: str = None
        self.test_div: int = None
        self.all_div: int = None
        self.test_pass: int = None
        self.test_fail: int = None
        self.total_inspections: int = 0

    def inspect(self):
        self.total_inspections += len(self.items)
        self.items = [int(self.operation(item)) for item in self.items]
        self.throw()

    def throw(self):
        for item in self.items:
            r = item % self.all_div
            if item % self.test_div:
                friend = self.friends[self.test_fail]
            else:
                friend = self.friends[self.test_pass]
            friend.items.append(r + self.all_div)
        self.items.clear()


def create_monkey(monkeys: list[Monkey], name: str):
    name = int(name.strip(":"))
    new_monkey = Monkey(name)
    for monkey in monkeys:
        monkey.friends[name] = new_monkey
        new_monkey.friends[monkey.name] = monkey
    monkeys.append(new_monkey)
    return monkeys


def assign_items(monkey: Monkey, items: list[str]):
    for i in range(2, len(items)):
        monkey.items.append(int(items[i].strip(",")))


def assign_operation(monkey: Monkey, line: list[str]):
    #   Operation: new = old + 8
    if line[4] == "+":
        if line[-1] == "old":
            monkey.operation = lambda x: int(x + x)
        else:
            monkey.operation = lambda x: int(x + int(line[-1]))
    else:
        if line[-1] == "old":
            monkey.operation = lambda x: int(x * x)
        else:
            monkey.operation = lambda x: int(x * int(line[-1]))


def parse(inp):
    monkeys = []
    with open(inp) as f:
        big_div = 1
        for l in f:
            l = l.strip().split()
            if not l:
                continue
            if l[0] == "Monkey":
                monkeys = create_monkey(monkeys, l[1])
            elif l[0] == "Starting":
                assign_items(monkeys[-1], l)
            elif l[0] == "Operation:":
                assign_operation(monkeys[-1], l)
            elif l[0] == "Test:":
                monkeys[-1].test_div = int(l[-1])
                big_div *= int(l[-1])
            elif l[1] == "true:":
                monkeys[-1].test_pass = int(l[-1])
            elif l[1] == "false:":
                monkeys[-1].test_fail = int(l[-1])
    for monkey in monkeys:
        monkey.all_div = big_div
    return monkeys


def play(monkeys: list[Monkey], rounds: int):
    for round in range(rounds):
        for monkey in monkeys:
            monkey.inspect()
    interactions = [monkey.total_inspections for monkey in monkeys]
    interactions.sort()
    print(interactions[-1] * interactions[-2])


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/11/input.txt"
    monkeys = parse(in_file)
    play(monkeys, 10_000)
