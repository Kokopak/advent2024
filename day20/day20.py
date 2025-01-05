import heapq
from collections import Counter

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


def get_shortcuts(maze):
    shortcuts = set()

    for coord in maze:
        if maze[coord] == "#":
            v1 = (coord[0] + 1, coord[1])
            v2 = (coord[0] - 1, coord[1])

            if v1 in maze and v2 in maze and maze[v1] != "#" and maze[v2] != "#":
                shortcuts.add((v1, v2))

            v1 = (coord[0], coord[1] + 1)
            v2 = (coord[0], coord[1] - 1)

            if v1 in maze and v2 in maze and maze[v1] != "#" and maze[v2] != "#":
                shortcuts.add((v1, v2))

    return shortcuts


d, prev = dijkstra(maze, start)
comp = d[target]
c = Counter()


shortcuts = get_shortcuts(maze)

for s in shortcuts:
    v1, v2 = s

    if v1 in d and v2 in d:
        if abs(d[v1] - d[v2]) - 2 >= 100:
            c[abs(d[v1] - d[v2]) - 2] += 1

print(c.total())
