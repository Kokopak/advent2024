from collections import OrderedDict

with open("input.txt") as f:
    disk_map = list(map(int, f.readline()))


files = disk_map[::2]
free_sizes = disk_map[1::2]

s = 0

total_index = 0
file_id = 0
file_max_id = len(files) - 1

while file_id < len(files):
    for i in range(files[file_id]):
        s += file_id * total_index

        total_index += 1

    while free_sizes[file_id] != 0 and (len(files) - 1 - file_id):
        files[-1] -= 1
        free_sizes[file_id] -= 1

        s += file_max_id * total_index

        if files[-1] == 0:
            files.pop()
            file_max_id -= 1

        total_index += 1

    file_id += 1


print(s)


full_map = []
i = 0
while disk_map:
    f = disk_map.pop(0)
    full_map.append([i] * f)

    if len(disk_map):
        size = disk_map.pop(0)
        full_map.append([-1] * size)

    i += 1


end = len(full_map) - 1

availables_size = OrderedDict(
    {ia: len(a) for ia, a in enumerate(full_map) if a and -1 in a}
)

for i in availables_size:
    full_map[i] = []


while end >= 0:
    find = False
    start = 0

    while len(full_map[end]) == 0 or full_map[end][0] == -1:
        end -= 1

    availables = [avs for avs in availables_size if avs < end]

    for a in availables:
        if availables_size[a] >= len(full_map[end]):
            full_map[a].extend(full_map[end])

            full_map[end] = [-1] * len(full_map[end])
            availables_size[a] -= len(full_map[end])

            if availables_size[a] <= 0:
                del availables_size[a]

            break
    else:
        end -= 1


for a in availables_size:
    full_map[a].extend([-1] * availables_size[a])

print(
    sum(f * i for i, f in enumerate(n for group in full_map for n in group) if f != -1)
)
