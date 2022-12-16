import functools


def find_num_end(l, idx):
    while l[idx].isnumeric():
        idx += 1
    return idx


def fill_list(l, idx):
    new_list = []
    while idx < len(l):
        if l[idx].isnumeric():
            next = find_num_end(l, idx)
            new_list.append(int(l[idx:next]))
            idx = next
        elif l[idx] == ",":
            idx += 1
        elif l[idx] == "[":
            nested, idx = fill_list(l, idx + 1)
            new_list.append(nested)
            idx += 1
        else:
            return new_list, idx
    return new_list, idx


def parse(inp):
    packets = []
    with open(inp) as f:
        for l in f:
            if l.isspace():
                continue
            l = l.strip()
            packet, _ = fill_list(l, 1)
            packets.append(packet)
    return packets


# decsion: -1 - correct; 1 - wrong; 0 - undecided
def compare_lists(left, right):
    i = 0
    while i < len(left) and i < len(right):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return -1
            elif left[i] > right[i]:
                return 1
            i += 1
        elif isinstance(left[i], list) and isinstance(right[i], list):
            decision = compare_lists(left[i], right[i])
            if decision == -1:
                return -1
            if decision == 1:
                return 1
            i += 1
        elif isinstance(left[i], int):
            decision = compare_lists([left[i]], right[i])
            if decision == -1:
                return -1
            if decision == 1:
                return 1
            i += 1
        elif isinstance(right[i], int):
            decision = compare_lists(left[i], [right[i]])
            if decision == -1:
                return -1
            if decision == 1:
                return 1
            i += 1
    if i == len(left) and i == len(right):
        return 0
    if i == len(left):
        return -1
    return 1


def process_packets(packets):
    divider1 = [[2]]
    divider2 = [[6]]
    packets.append(divider1)
    packets.append(divider2)
    packets.sort(key=functools.cmp_to_key(compare_lists))
    print((1 + packets.index(divider1)) * (1 + packets.index(divider2)))


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/13/input.txt"
    packets = parse(in_file)

    process_packets(packets)
