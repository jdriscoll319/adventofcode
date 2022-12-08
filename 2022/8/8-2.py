def convert_input(input):
    grid = []
    with open(input) as f:
        for l in f:
            grid.append([int(i) for i in l.strip()])
    return grid


def scan_up(grid, r, c):
    val = grid[r][c]
    distance = 0
    for i in range(r - 1, -1, -1):
        if grid[i][c] >= val:
            return r - i
    return r


def scan_down(grid, r, c):
    val = grid[r][c]
    distance = 0
    for i in range(r + 1, len(grid)):
        if grid[i][c] >= val:
            return i - r
    return len(grid) - r - 1


def scan_left(grid, r, c):
    val = grid[r][c]
    distance = 0
    for i in range(c - 1, -1, -1):
        if grid[r][i] >= val:
            return c - i
    return c


def scan_right(grid, r, c):
    val = grid[r][c]
    distance = 0
    for i in range(c + 1, len(grid[r])):
        if grid[r][i] >= val:
            return i - c
    return len(grid[r]) - c - 1


def scan_grid(grid):
    max_score = 0
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[r]) - 1):
            up = scan_up(grid, r, c)
            down = scan_down(grid, r, c)
            left = scan_left(grid, r, c)
            right = scan_right(grid, r, c)
            if up * down * left * right > max_score:
                max_score = up * down * left * right

    return max_score


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/8/input.txt"
    grid = convert_input(in_file)
    print(scan_grid(grid))
