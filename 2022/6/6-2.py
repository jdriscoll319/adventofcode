# mjqjpqmgbljsphdztnvjfqwrcgsmlb
def start_of_packet(line):
    end = 1
    start = 0
    key = line[start]
    while end < len(line):
        if line[end] in line[start:end]:
            start += 1
            end = start + 1
        elif end - start == 13:
            return end + 1
        else:
            end += 1


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/6/input.txt"
    line = ""
    with open(in_file) as f:
        line = f.readline().strip()

    print(start_of_packet(line))
