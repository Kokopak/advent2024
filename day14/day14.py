import re
from collections import defaultdict

with open("input.txt") as f:
    robots = []
    regex = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
    grid = defaultdict(int)

    for l in f.readlines():
        x, y, vx, vy = regex.findall(l)[0]
        robots.append({"x": int(x), "y": int(y), "vx": int(vx), "vy": int(vy)})
        grid[(int(x), int(y))] += 1


W = 100
H = 102


for i in range(7000):
    draw = True

    if i == 100:
        q1 = q2 = q3 = q4 = 0

        for r in robots:
            if r["x"] != W // 2 and r["y"] != H // 2:
                if r["x"] < W // 2 and r["y"] < H // 2:
                    q1 += 1

                if r["x"] > W // 2 and r["y"] < H // 2:
                    q2 += 1

                if r["x"] < W // 2 and r["y"] > H // 2:
                    q3 += 1

                if r["x"] > W // 2 and r["y"] > H // 2:
                    q4 += 1

        print(q1 * q2 * q3 * q4)

    for r in robots:
        grid[(r["x"], r["y"])] -= 1

        r["x"] = (r["x"] + r["vx"]) % (W + 1)
        r["y"] = (r["y"] + r["vy"]) % (H + 1)

        grid[(r["x"], r["y"])] += 1

    if all(grid[k] <= 1 for k in grid):
        print(i + 1)
        for y in range(H + 1):
            print("")
            for x in range(W + 1):
                if grid[(x, y)] > 0:
                    print(grid[(x, y)], end="")
                else:
                    print(".", end="")
