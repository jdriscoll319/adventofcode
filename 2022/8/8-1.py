def convert_input(input):
    grid = []
    with open(input) as f:
        for l in f:
            grid.append([int(i) for i in l.strip()])
    return grid


def scan_up(grid, r, c):
    val = grid[r][c]
    for i in range(r - 1, -1, -1):
        if grid[i][c] >= val:
            return False
    return True


def scan_down(grid, r, c):
    val = grid[r][c]
    for i in range(r + 1, len(grid)):
        if grid[i][c] >= val:
            return False
    return True


def scan_left(grid, r, c):
    val = grid[r][c]
    for i in range(c - 1, -1, -1):
        if grid[r][i] >= val:
            return False
    return True


def scan_right(grid, r, c):
    val = grid[r][c]
    for i in range(c + 1, len(grid[r])):
        if grid[r][i] >= val:
            return False
    return True


def scan_grid(grid):
    visibility = 0
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[r]) - 1):
            if scan_up(grid, r, c):
                visibility += 1
            elif scan_down(grid, r, c):
                visibility += 1
            elif scan_left(grid, r, c):
                visibility += 1
            elif scan_right(grid, r, c):
                visibility += 1

    return visibility


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/8/input.txt"
    grid = convert_input(in_file)
    visibility = len(grid) * 2 + (len(grid[0]) - 2) * 2
    visibility += scan_grid(grid)
    print(visibility)
