# f = open('./example.txt', 'r')
f = open('./input.txt', 'r')

lines = f.readlines()
antennas_map = [list(l.strip()) for l in lines]
w = len(antennas_map[0])
h = len(antennas_map)

antinodes_map = [["." for _ in l] for l in antennas_map]

antennas_list = []
for y in range(h):
    for x in range(w):
        if antennas_map[y][x] != '.':
            antennas_list.append((antennas_map[y][x], y, x))
            antinodes_map[y][x] = '#'


def out_of_bounds(x, y):
    return x < 0 or y < 0 or x >= w or y >= h


def check_antenna(l):
    for (c2, y2, x2) in l[1:]:
        (c1, y1, x1) = l[0]
        if c1 == c2:
            dx = x1 - x2
            dy = y1 - y2
            while not out_of_bounds(x1 + dx, y1 + dy):
                antinodes_map[y1+dy][x1+dx] = '#'
                x1 += dx
                y1 += dy
            while not out_of_bounds(x2 - dx, y2 - dy):
                antinodes_map[y2-dy][x2-dx] = '#'
                x2 -= dx
                y2 -= dy


for i in range(len(antennas_list)-1):
    check_antenna(antennas_list[i:])

antinodes = sum([l.count('#') for l in antinodes_map])

print(antennas_list)
print('\n'.join([''.join(l) for l in antennas_map]))
print('\n'.join([''.join(l) for l in antinodes_map]))
print("nbr of antinodes: " + str(antinodes))
