# f = open('./example.txt', 'r')
f = open('./input.txt', 'r')

line = f.readline().strip()

used_map = []
free_map = []
disk_map = []
I = 0
for i in range(len(line)):
    if i % 2 == 0:
        used_map.append((I, int(line[i]), str(i//2)))
    else:
        free_map.append((I, int(line[i])))
    for _ in range(int(line[i])):
        I += 1
        if i % 2 == 0:
            disk_map.append(str(i//2))
        else:
            disk_map.append('.')

print(''.join(disk_map))

used_map.reverse()
for (u_i, u_len, Id) in used_map:
    i = 0
    (f_i, f_len) = free_map[i]
    while f_len < u_len and f_i < u_i and i+1 < len(free_map):
        i += 1
        (f_i, f_len) = free_map[i]
    if f_len >= u_len:
        free_map[i] = (f_i + u_len, f_len - u_len)
        for j in range(f_i, f_i + u_len):
            disk_map[j] = Id
        for j in range(u_i, u_i + u_len):
            disk_map[j] = '.'


print(''.join(disk_map))

res = 0
i = 0
while i < len(disk_map):
    if disk_map[i] != '.':
        res += int(disk_map[i]) * i
    i += 1

print("check-sum: " + str(res))
