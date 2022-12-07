from dataclasses import dataclass, field


@dataclass
class dir:
    name: str
    parent: dir = None
    subdirs: dict = field(default_factory=dict)
    files: dict = field(default_factory=dict)
    size: int = 0


def cd(new_dir: str, cur_dir: dir, head):
    if new_dir == "..":
        return cur_dir.parent

    if new_dir == "/":
        return head

    # Assume input doesn't end up here before explicitly stating that this dir exists
    return cur_dir.subdirs[new_dir]


def calculate_sizes(cur_dir: dir, total_sum: int):
    for sd in cur_dir.subdirs.values():
        total_sum = calculate_sizes(sd, total_sum)
        cur_dir.size += sd.size

    if cur_dir.size < 100_000:
        return total_sum + cur_dir.size

    return total_sum


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/7/input.txt"
    head = dir(name="/")
    cur_dir = head
    with open(in_file) as f:
        for l in f:
            l = l.strip().split()
            if l[0] == "$":
                if l[1] == "cd":
                    cur_dir = cd(l[2], cur_dir, head)
                else:
                    continue
            elif l[0] == "dir":
                if l[1] not in cur_dir.subdirs:
                    cur_dir.subdirs[l[1]] = dir(name=l[1], parent=cur_dir)
            elif l[0].isnumeric():
                if l[1] not in cur_dir.files:
                    cur_dir.files[l[1]] = int(l[0])
                    cur_dir.size += int(l[0])

    # At this point each dir only contains it's direct size
    # ie dir.size does not take into account size of any subdirs
    total = calculate_sizes(head, 0)
    print(total)
