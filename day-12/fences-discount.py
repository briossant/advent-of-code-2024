# f = open('./example.txt', 'r')
# f = open('./example-2.txt', 'r')
f = open('./input.txt', 'r')

lines = f.readlines()
Map = [list(l.strip()) for l in lines]
w = len(Map[0])
h = len(Map)


def out_of_bounds(x, y):
    return x < 0 or y < 0 or x >= w or y >= h


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def Id(dx, dy):
    return str(dx+1 + 2*(dy+1))


def Border(x, y, dx, dy, c):
    iid = Id(dx, dy)
    Dx = abs(dx) - 1
    Dy = abs(dy) - 1

    X, Y = x+Dx, y+Dy
    while not out_of_bounds(X, Y) and Map[Y][X].count(c):
        if not out_of_bounds(X+dx, Y+dy) and (Map[Y+dy][X+dx].count(c)
                                              or Map[Y+dy][X+dx] == '*'):
            break
        Map[Y][X] += iid
        X += Dx
        Y += Dy

    X, Y = x-Dx, y-Dy
    while not out_of_bounds(X, Y) and Map[Y][X].count(c):
        if not out_of_bounds(X+dx, Y+dy) and (Map[Y+dy][X+dx].count(c)
                                              or Map[Y+dy][X+dx] == '*'):
            break
        Map[Y][X] += iid
        X -= Dx
        Y -= Dy


def explore(x, y, c):
    om = Map[y][x]
    Map[y][x] = '*'
    a, p = 1, 0

    for dx, dy in dirs:
        X, Y = x+dx, y+dy
        if out_of_bounds(X, Y):
            if om.count(Id(dx, dy)) == 0:
                print(x, y, om, Id(dx, dy), "out")
                Border(x, y, dx, dy, c)
                p += 1
        elif Map[Y][X].count(c) == 0 and Map[Y][X] != '*':
            if om != '*' and om.count(Id(dx, dy)) == 0:
                print(x, y, om, Id(dx, dy), "in")
                Border(x, y, dx, dy, c)
                p += 1

    for dx, dy in dirs:
        X, Y = x+dx, y+dy
        if not out_of_bounds(X, Y) and Map[Y][X].count(c):
            (da, dp) = explore(X, Y, c)
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
