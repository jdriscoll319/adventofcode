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


def update_parent_size(cur_dir: dir, size: int):
    cur_dir.size += size
    if cur_dir.parent:
        update_parent_size(cur_dir.parent, size)


def find_dir(cur_dir: dir, target: int, current_solution: int):
    for sd in cur_dir.subdirs.values():
        current_solution = find_dir(sd, target, current_solution)

    if cur_dir.size >= target and cur_dir.size < current_solution:
        return cur_dir.size

    return current_solution


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
                    update_parent_size(cur_dir, int(l[0]))

    total_ds = 70_000_000
    needed_ds = 30_000_000
    current_ds = head.size
    remaining = total_ds - current_ds
    target = needed_ds - remaining
    dir_size = find_dir(head, target, current_ds)
    print(dir_size)
