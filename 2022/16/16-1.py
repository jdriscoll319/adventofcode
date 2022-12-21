from dataclasses import dataclass, field
from queue import PriorityQueue


class Valve:
    def __init__(self, name) -> None:
        self.name: str = name
        self.tunnels: dict[str, Valve] = {}
        self.weights: dict[str, int] = {}
        self.shortest_path: dict[str, int] = {}
        self.flow_rate = None
        self.is_on = False
        self.time_on = 0

    def remove_neighbor(self, neighbor):
        for name, valve in neighbor.tunnels.items():
            if name != self.name:
                self.tunnels[name] = valve
                self.weights[name] = (
                    self.weights[neighbor.name] + neighbor.weights[name]
                )
        del self.tunnels[neighbor.name]
        del self.weights[neighbor.name]


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    valve: Valve = field(compare=False)


def parse(inp):
    valves: dict[str, Valve] = {}
    with open(inp) as f:
        for l in f:
            l = l.strip().replace(";", "").replace(",", "").split()
            name = l[1]
            if name not in valves:
                valves[name] = Valve(name)
            flow_rate = l[4]
            flow_rate = flow_rate[flow_rate.find("=") + 1 :]
            valves[name].flow_rate = int(flow_rate)
            for i in range(9, len(l)):
                tunnel = l[i]
                if tunnel not in valves:
                    valves[tunnel] = Valve(tunnel)
                valves[name].tunnels[tunnel] = valves[tunnel]
                valves[name].weights[tunnel] = 1
    return valves


def collapse(valves: dict[str, Valve]) -> dict[str, Valve]:
    new_valves = {}
    for name, valve in valves.items():
        if name != "AA" and valve.flow_rate == 0:
            for neighbor in valve.tunnels.values():
                neighbor.remove_neighbor(valve)
        else:
            new_valves[name] = valve
    return new_valves


def shortest_path(source: Valve, target: Valve):
    if target.name in source.shortest_path:
        return source.shortest_path[target.name]

    p_queue = PriorityQueue()
    p_queue.put(PrioritizedItem(0, source))
    came_from = {}
    explored = set()
    score = {source.name: 0}

    while not p_queue.empty():
        cur_pos = p_queue.get().valve
        if cur_pos.name == target.name:
            source.shortest_path[target.name] = score[target.name]
            target.shortest_path[source.name] = score[target.name]
            return score[target.name]
        if cur_pos.name in explored:
            continue
        explored.add(cur_pos.name)
        for neighbor in cur_pos.tunnels.values():
            node_score = cur_pos.weights[neighbor.name] + score[cur_pos.name]
            if neighbor not in score or node_score < score[neighbor]:
                score[neighbor.name] = node_score
                came_from[neighbor.name] = cur_pos.name
                # p_queue.put((node_score, neighbor))
                p_queue.put(PrioritizedItem(node_score, neighbor))


def explore(
    cur_pos: Valve,
    still_closed: list[str],
    valves: dict[str, Valve],
    time_left,
    score,
    max_score,
):
    if time_left <= 1:
        return max(score, max_score)
    if cur_pos.flow_rate:
        time_left -= 1
        score += time_left * cur_pos.flow_rate
    for i, name in enumerate(still_closed):
        travel_time = shortest_path(cur_pos, valves[name])
        max_score = explore(
            valves[name],
            still_closed[:i] + still_closed[i + 1 :],
            valves,
            time_left - travel_time,
            score,
            max_score,
        )
    return max(score, max_score)


def get_score(valves: dict[str, Valve]):
    time_left = 30
    cur_pos = valves["AA"]
    still_closed = [valve.name for valve in valves.values() if valve.flow_rate > 0]
    score = explore(cur_pos, still_closed, valves, time_left, 0, 0)
    print(score)


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/16/input.txt"
    valves = parse(in_file)
    # Seems to be broken for the full input...
    # valves = collapse(valves)
    get_score(valves)
