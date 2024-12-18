import heapq

with open("input.txt") as f:
    ROWS = 71
    COLS = 71
    BYTES = 12

    bytes_coord = [(int(l.split(",")[0]), int(l.split(",")[1])) for l in f.readlines()]


def get_neighbors(maze, u):
    neighbors = set()

    for dv in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        v = (u[0] + dv[0], u[1] + dv[1])
        if v in maze and maze[v] == ".":
            neighbors.add(v)

    return neighbors


def dijkstra(maze, start, dist={}):
    q = []
    dist = dist if dist else {}

    dist[start] = 0

    heapq.heappush(q, (0, start))

    while q:
        _, u = heapq.heappop(q)

        neighbors = get_neighbors(maze, u)

        for v in neighbors:
            alt = dist[u] + 1

            if alt < dist.get(v, float("inf")) and maze[v] != "#":
                dist[v] = alt

                heapq.heappush(q, (alt, v))

    return dist


grid = {}

for y in range(ROWS):
    for x in range(COLS):
        grid[(x, y)] = "."

for i, b in enumerate(bytes_coord):
    if i == 1024:
        break

    grid[b] = "#"

d = dijkstra(grid, (0, 0))
print(d[(70, 70)])

for y in range(ROWS):
    for x in range(COLS):
        grid[(x, y)] = "."

while bytes_coord:
    byte_coord = bytes_coord.pop(0)
    grid[byte_coord] = "#"

    if byte_coord not in d:
        continue

    d = dijkstra(grid, (0, 0))

    if (70, 70) not in d:
        break


print(byte_coord)
