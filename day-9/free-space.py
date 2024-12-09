# f = open('./example.txt', 'r')
f = open('./input.txt', 'r')

line = f.readline().strip()

disk_map = []
for i in range(len(line)):
    for _ in range(int(line[i])):
        if i % 2 == 0:
            disk_map.append(str(i//2))
        else:
            disk_map.append('.')

print(''.join(disk_map))

i = 0
j = len(disk_map)-1
while i < j:
    while i < j and disk_map[i] != '.':
        i += 1
    while i < j and disk_map[j] == '.':
        j -= 1
    if i < j:
        disk_map[i], disk_map[j] = disk_map[j], disk_map[i]

print(''.join(disk_map))

res = 0
i = 0
while i < len(disk_map) and disk_map[i] != '.':
    res += int(disk_map[i]) * i
    i += 1

print("check-sum: " + str(res))
