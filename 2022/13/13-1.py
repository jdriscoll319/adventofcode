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
    packets = {}
    cur_pair = 1
    cur_packet = 0
    with open(inp) as f:
        packet1, packet2 = [], []
        for l in f:
            if l.isspace():
                packets[cur_pair] = [packet1, packet2]
                cur_pair += 1
                continue
            l = l.strip()
            if cur_packet == 0:
                packet1, _ = fill_list(l, 1)
                cur_packet = 1
            else:
                packet2, _ = fill_list(l, 1)
                cur_packet = 0
        packets[cur_pair] = [packet1, packet2]
    return packets


# decsion: 1 - correct; 2 - wrong; 3 - undecided
def compare_lists(left, right, tab):
    i = 0
    # print(f"{'':{tab * 2}}- Compare {left} vs {right}")
    while i < len(left) and i < len(right):
        if isinstance(left[i], int) and isinstance(right[i], int):
            # print(f"{'':{tab * 2 + 2}}- Compare {left[i]} vs {right[i]}")
            if left[i] < right[i]:
                # print(
                # f"{'':{tab * 2 + 4}}- Left side is smaller, so inputs are in the right order"
                # )
                return 1
            elif left[i] > right[i]:
                # print(
                # f"{'':{tab * 2 + 4}}- Right side is smaller, so inputs are not in the right order"
                # )
                return 2
            i += 1
        elif isinstance(left[i], list) and isinstance(right[i], list):
            decision = compare_lists(left[i], right[i], tab + 1)
            if decision == 1:
                return 1
            if decision == 2:
                return 2
            i += 1
        elif isinstance(left[i], int):
            # print(f"{'':{tab * 2 + 2}}- Compare {left[i]} vs {right[i]}")
            # print(
            # f"{'':{tab * 2 + 4}}- Mixed types; convert left to [{left[i]}] and retry comparison"
            # )
            decision = compare_lists([left[i]], right[i], tab + 2)
            if decision == 1:
                return 1
            if decision == 2:
                return 2
            i += 1
        elif isinstance(right[i], int):
            # print(f"{'':{tab * 2 + 2}}- Compare {left[i]} vs {right[i]}")
            # print(
            # f"{'':{tab * 2 + 4}}- Mixed types; convert right to [{right[i]}] and retry comparison"
            # )
            decision = compare_lists(left[i], [right[i]], tab + 2)
            if decision == 1:
                return 1
            if decision == 2:
                return 2
            i += 1
    if i == len(left) and i == len(right):
        return 3
    if i == len(left):
        # print(
        # f"{'':{tab * 2 + 2}}- Left side ran out of items, so inputs are in the right order"
        # )
        return 1
    # print(
    # f"{'':{tab * 2 + 2}}- Right side ran out of items, so inputs are not in the right order"
    # )
    return 2


def process_packets(packets):
    sum = 0
    for key, val in packets.items():
        # print(f"== Pair {key} ==")
        decision = compare_lists(val[0], val[1], 0)
        if decision == 1:  # in [1, 3]:
            # print(f"Adding {key}")
            sum += key
        if decision == 3:
            print("ERROR: Every input should have a decision")
        # print()
    print(sum)


def copy(file, packets):
    with open(file, "w") as f:
        for packet in packets.values():
            f.write(str(packet[0]).replace(" ", "") + "\n")
            f.write(str(packet[1]).replace(" ", "") + "\n")
            f.write("\n")


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/13/input.txt"
    copy_file = "/home/adam/projects/adventofcode/2022/13/copy.txt"
    packets = parse(in_file)
    # copy(copy_file, packets)

    process_packets(packets)
