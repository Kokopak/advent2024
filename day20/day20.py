import heapq
from collections import Counter
from functools import partial
from multiprocessing import Pool

with open("input.txt") as f:
    maze = {}
    start = (0, 0)
    target = (0, 0)
    for irow, row in enumerate(f.readlines()):
        for icol, col in enumerate(row):
            maze[(irow, icol)] = col.strip()

            if col == "S":
                start = (irow, icol)
            if col == "E":
                target = (irow, icol)

    ROWS = irow + 1
    COLS = icol + 1


def get_neighbors(maze, u):
    neighbors = set()

    for dv in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        v = (u[0] + dv[0], u[1] + dv[1])

        if v in maze:
            neighbors.add(v)

    return neighbors


def dijkstra(maze, start, dist={}):
    q = []
    dist = dist if dist else {start: 0}
    prev = {}

    for k in dist:
        heapq.heappush(q, (dist[k], k))

    heapq.heappush(q, (0, start))

    while q:
        _, u = heapq.heappop(q)
        neighbors = get_neighbors(maze, u)

        for v in neighbors:
            if maze[v] != "#":
                alt = dist[u] + 1

                if alt < dist.get(v, float("inf")):
                    dist[v] = alt
                    prev[v] = u

                    heapq.heappush(q, (alt, v))

    return dist, prev


def manhattan(coord1, coord2):
    return abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])


d, prev = dijkstra(maze, start)
comp = d[target]


def process_coord(coord, cheat_length, threshold):
    c = Counter()

    for dr in range(-cheat_length, cheat_length + 1):
        for dc in range(-cheat_length, cheat_length + 1):
            coord2 = (coord[0] + dr, coord[1] + dc)

            if coord2 in d:
                length = manhattan(coord, coord2)

                if length <= cheat_length:
                    save_steps = abs(d[coord] - d[coord2]) - length

                    if save_steps >= threshold:
                        c[save_steps] += 1

    return c.total()


with Pool() as p:
    print(sum(p.map(partial(process_coord, cheat_length=2, threshold=100), d)) // 2)
    print(sum(p.map(partial(process_coord, cheat_length=20, threshold=100), d)) // 2)
