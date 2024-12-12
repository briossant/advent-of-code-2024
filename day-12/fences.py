# f = open('./example.txt', 'r')
f = open('./input.txt', 'r')

lines = f.readlines()
Map = [list(l.strip()) for l in lines]
w = len(Map[0])
h = len(Map)


def out_of_bounds(x, y):
    return x < 0 or y < 0 or x >= w or y >= h


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def explore(x, y, c):
    if out_of_bounds(x, y):
        return (0, 1)
    if Map[y][x] != c:
        return (0, 0 if Map[y][x] == '*' else 1)

    Map[y][x] = '*'
    a, p = 1, 0

    for dx, dy in dirs:
        (da, dp) = explore(x+dx, y+dy, c)
        a += da
        p += dp
    return (a, p)


res = 0
for y in range(h):
    for x in range(w):
        if Map[y][x] != '#':
            (a, p) = explore(x, y, Map[y][x])
            print(str(a) + "*" + str(p) + " = " + str(a*p))
            res += a*p
            Map = [['#' if x == '*' else x for x in l] for l in Map]

print("fences cost: ", str(res))
