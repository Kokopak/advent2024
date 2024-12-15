MAP_DIR = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

with open("input.txt") as f:
    grid_str, instructions_str = f.read().strip().split("\n\n")
    instructions = ""
    for i in instructions_str.strip():
        instructions += i.strip()

    grid = {}
    blocks = set()

    for irow, row in enumerate(grid_str.strip().split("\n")):
        for icol, col in enumerate(row):
            grid[(irow, icol)] = col

            if col == "@":
                robot = (irow, icol)
            elif col == "O":
                blocks.add((irow, icol))

    ROWS = irow + 1
    COLS = icol + 1

for inst in instructions:
    mapped_dir = MAP_DIR[inst]
    next_move = (robot[0] + mapped_dir[0], robot[1] + mapped_dir[1])

    move = True

    if not grid[next_move] == "#":
        if grid[next_move] == "O":
            blocks_to_push = []
            r_move, c_move = next_move

            while grid[(r_move, c_move)] != ".":
                if grid[(r_move, c_move)] == "#":
                    break
                blocks_to_push.append((r_move, c_move))

                r_move, c_move = r_move + mapped_dir[0], c_move + mapped_dir[1]

            if (
                not grid[
                    (
                        blocks_to_push[-1][0] + mapped_dir[0],
                        blocks_to_push[-1][1] + mapped_dir[1],
                    )
                ]
                == "#"
            ):
                for block in blocks_to_push[::-1]:
                    grid[(block[0], block[1])] = "."
                    grid[(block[0] + mapped_dir[0], block[1] + mapped_dir[1])] = "O"
            else:
                move = False

        if move:
            grid[robot] = "."
            robot = next_move
            grid[robot] = "@"

s = 0
for coord in grid:
    if grid[coord] == "O":
        s += 100 * coord[0] + coord[1]

print(s)
