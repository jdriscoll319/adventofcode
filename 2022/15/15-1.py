def parse(inp):
    sensor_to_beacon = {}
    sensor_range = {}
    with open(inp) as f:

        for l in f:
            ind = l.find("=") + 1
            end = l.find(",", ind)
            sx = int(l[ind:end])
            ind = end + 4
            end = l.find(":", ind)
            sy = int(l[ind:end])
            ind = l.find("=", end) + 1
            end = l.find(",", ind)
            bx = int(l[ind:end])
            ind = end + 4
            by = int(l[ind:].strip())
            sensor_to_beacon[(sx, sy)] = (bx, by)
            sensor_range[(sx, sy)] = abs(sx - bx) + abs(sy - by)
    return sensor_to_beacon, sensor_range


def find_scanned(sensor_to_beacon, sensor_range):
    scanned = set()
    row = 2_000_000
    for sensor, beacon in sensor_to_beacon.items():
        dist = sensor_range[sensor]
        num_intersections = max(0, (dist - abs(row - sensor[1])) * 2 + 1)
        if num_intersections:
            x = sensor[0]
            half_range = int((num_intersections - 1) / 2)
            for i in range(x - half_range, x + half_range + 1):
                scanned.add((i, row))
        beacon in scanned and scanned.remove(beacon)

    print(len(scanned))


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/15/input.txt"
    sensor_to_beacon, sensor_range = parse(in_file)
    find_scanned(sensor_to_beacon, sensor_range)
