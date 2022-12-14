import string
from queue import PriorityQueue


def get_priority(pos, neighbor):
    if pos == "S":
        pos = "a"
    elif pos == "E":
        pos = "z"
    if neighbor == "S":
        neighbor = "a"
    elif neighbor == "E":
        neighbor = "z"
    val = string.ascii_letters.index(neighbor) - string.ascii_letters.index(pos)
    if val >= 2:
        return 0
    if val <= 0:
        val = val * -1 + 2
    return val


def get_neighbors(pos, grid):
    neighbors = []
    if pos[0] > 0:
        neighbors.append((pos[0] - 1, pos[1]))
    if pos[0] < len(grid) - 1:
        neighbors.append((pos[0] + 1, pos[1]))
    if pos[1] > 0:
        neighbors.append((pos[0], pos[1] - 1))
    if pos[1] < len(grid[0]) - 1:
        neighbors.append((pos[0], pos[1] + 1))

    return neighbors


def find_path(grid, starts, end):
    min_steps = None

    for start in starts:
        p_queue = PriorityQueue()
        p_queue.put((0, start))
        came_from = {}
        explored = set()
        score = {start: 0}

        while not p_queue.empty():
            cur_pos = p_queue.get()[1]
            if cur_pos == end:
                if min_steps:
                    min_steps = min(min_steps, score[end])
                else:
                    min_steps = score[end]
                break
            if min_steps and score[cur_pos] > min_steps:
                break
            if cur_pos in explored:
                continue
            explored.add(cur_pos)
            for neighbor in get_neighbors(cur_pos, grid):
                priority = get_priority(
                    grid[cur_pos[0]][cur_pos[1]], grid[neighbor[0]][neighbor[1]]
                )
                if not priority:
                    continue
                node_score = 1 + score[cur_pos]
                if neighbor not in score or node_score < score[neighbor]:
                    score[neighbor] = node_score
                    came_from[neighbor] = cur_pos
                    p_queue.put((node_score, neighbor))
    print(min_steps)


def parse(inp):
    start = None
    end = None
    grid = []
    row = 0
    starts = []
    with open(inp) as f:
        for l in f:
            cur = []
            if "E" in l:
                end = (row, l.find("E"))
            for idx, c in enumerate(l.strip()):
                if c in "Sa":
                    starts.append((row, idx))
                cur.append(c)
            grid.append(cur)
            row += 1
    return grid, starts, end


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/12/input.txt"
    grid, start, end = parse(in_file)
    find_path(grid, start, end)
