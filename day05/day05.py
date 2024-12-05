import functools

with open("input.txt") as f:
    rules, updates = f.read().split("\n\n")

    rules = rules.splitlines()
    updates = updates.splitlines()


s = 0
s2 = 0


def cmp(a, b):
    if f"{a}|{b}" in rules:
        return -1
    elif f"{b}|{a}" in rules:
        return 1
    else:
        return 0


for u in updates:
    u_spl = u.split(",")
    u_pairs = list(zip(u_spl, u_spl[1:]))

    for i, p in enumerate(u_pairs):
        if "|".join(p) not in rules:
            sorted_u = sorted(u_spl, key=functools.cmp_to_key(cmp))
            s2 += int(sorted_u[len(sorted_u) // 2])
            break
    else:
        s += int(u_spl[len(u_spl) // 2])

print(s)
print(s2)
