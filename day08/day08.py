from collections import defaultdict

with open("input.txt") as f:
    grid = {}
    pairs = defaultdict(list)

    for ir, r in enumerate(f.readlines()):
        for ic, c in enumerate(r.strip()):
            if c != ".":
                pairs[c].append((ir, ic))

    ROWS = ir + 1
    COLS = ic + 1

pairs = [
    (p, p1) for k in pairs for i, p in enumerate(pairs[k]) for p1 in pairs[k][i + 1 :]
]

antinodes = set()

for p in pairs:
    (dr, dc) = (p[0][0] - p[1][0], p[0][1] - p[1][1])

    for new in [(p[0][0] + dr, p[0][1] + dc), (p[1][0] - dr, p[1][1] - dc)]:
        if new[0] < ROWS and new[1] < COLS and new[0] >= 0 and new[1] >= 0:
            antinodes.add(new)


print(len(antinodes))

antinodes = set()

for p in pairs:
    (dr, dc) = (p[0][0] - p[1][0], p[0][1] - p[1][1])

    for new in [[p[0][0] + dr, p[0][1] + dc], [p[1][0] - dr, p[1][1] - dc]]:
        while new[0] >= 0 and new[1] >= 0 and new[0] < ROWS and new[1] < COLS:
            antinodes.add(tuple(new))
            new[0] += dr
            new[1] += dc

        dr = -dr
        dc = -dc

    antinodes.add(p[0])
    antinodes.add(p[1])

print(len(antinodes))
