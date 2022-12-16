import numpy as np


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
    return sensor_range


def out_of_range(sensor, range):
    sensor = np.array(sensor)
    coords = []
    x = np.arange(0, range + 2)
    y = np.flip(x)
    dists = np.stack((x, y), axis=-1)
    coords.append(sensor + dists)
    coords.append(sensor + dists * [-1, 1])
    coords.append(sensor + dists * [1, -1])
    coords.append(sensor + dists * [-1, -1])
    coords = np.array(coords).reshape([-1, 2])
    coords = coords[np.all(coords <= 4_000_000, axis=1)]
    coords = coords[np.all(coords >= 0, axis=1)]
    return coords


def not_scanned_by_sensors(coords, sensor_range):
    for sensor, dist in sensor_range.items():
        if not len(coords):
            return coords
        coords = coords[np.sum(np.abs(sensor - coords), axis=-1) > dist]
    return coords


def find_hidden_beacon(sensor_range):
    for sensor, dist in sensor_range.items():
        coords = out_of_range(sensor, dist)
        coords = not_scanned_by_sensors(coords, sensor_range)
        if len(coords):
            print(coords[0, 0] * 4_000_000 + coords[0, 1])
            return


if __name__ == "__main__":
    in_file = "/home/adam/projects/adventofcode/2022/15/input.txt"
    sensor_range = parse(in_file)
    find_hidden_beacon(sensor_range)
