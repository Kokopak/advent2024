with open("input.txt") as f:
    words = [list(l.strip()) for l in f]

rows, cols = (len(words), len(words[0]))

counter = 0
counter2 = 0

for i in range(rows * cols):
    r = i // cols
    c = (i - cols) % cols

    # part 1
    poss = ["", "", "", ""]

    if c + 3 < cols:
        poss[1] = words[r][c] + words[r][c + 1] + words[r][c + 2] + words[r][c + 3]

    if r + 3 < rows:
        poss[0] = words[r][c] + words[r + 1][c] + words[r + 2][c] + words[r + 3][c]

        if c + 3 < cols:
            poss[2] = (
                words[r][c]
                + words[r + 1][c + 1]
                + words[r + 2][c + 2]
                + words[r + 3][c + 3]
            )

        if c - 3 >= 0:
            poss[3] = (
                words[r][c]
                + words[r + 1][c - 1]
                + words[r + 2][c - 2]
                + words[r + 3][c - 3]
            )

    for p in poss:
        if p == "XMAS" or p[::-1] == "XMAS":
            counter += 1

    # part 2
    poss2 = ["", ""]

    if words[r][c] == "A":
        if r - 1 >= 0 and c - 1 >= 0 and r + 1 < rows and c + 1 < cols:
            poss2[0] = words[r - 1][c - 1] + words[r][c] + words[r + 1][c + 1]
            poss2[1] = words[r - 1][c + 1] + words[r][c] + words[r + 1][c - 1]

        if poss2[0] == "MAS" and poss2[1] == "MAS":
            counter2 += 1

        if poss2[0] == "SAM" and poss2[1] == "SAM":
            counter2 += 1

        if poss2[0] == "SAM" and poss2[1] == "MAS":
            counter2 += 1

        if poss2[0] == "MAS" and poss2[1] == "SAM":
            counter2 += 1

print(counter)
print(counter2)
