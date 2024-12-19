with open("input.txt") as f:
    stripes = f.readline().strip().split(", ")
    f.readline()
    towels = [l.strip() for l in f.readlines()]


def can_match_design(design, patterns, memo):
    if design in memo:
        return memo[design]

    if not design:
        return True

    for pattern in patterns:
        if design.startswith(pattern):
            if can_match_design(design[len(pattern) :], patterns, memo):
                memo[design] = True
                return True

    memo[design] = False

    return False


def can_match_design_p2(design, patterns, memo):
    if design in memo:
        return memo[design]

    if not design:
        return 1

    total = 0

    for pattern in patterns:
        if design.startswith(pattern):
            total += can_match_design_p2(design[len(pattern) :], patterns, memo)

    memo[design] = total

    return total


s = 0
s2 = 0
for towel in towels:
    s += can_match_design(towel, stripes, {})
    s2 += can_match_design_p2(towel, stripes, {})

print(s)
print(s2)
