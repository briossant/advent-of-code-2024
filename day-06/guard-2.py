# f = open('./example.txt', 'r')
f = open('./input.txt', 'r')

lines = f.readlines()
lines = [list(l.strip()) for l in lines]
w = len(lines[0])
h = len(lines)

x = 0
y = 0
for i in range(h):
    if lines[i].count('^'):
        x = lines[i].index('^')
        y = i
        lines[y][x] = 'X'
        break

d = 0


def move(x, y, d):
    match d:
        case 0:
            y -= 1
        case 1:
            x += 1
        case 2:
            y += 1
        case 3:
            x -= 1
    return x, y


def out_of_bounds(x, y):
    return x < 0 or y < 0 or x >= w or y >= h


c = ['^', '>', 'v', '<']


def check_loop(X, Y, D):
    checked = set()
    stx, sty = move(X, Y, D)

    if lines[sty][stx] == '#':
        raise ValueError('Non non')
    if lines[sty][stx] == 'O' or lines[sty][stx] == 'X':
        return

    lines[sty][stx] = '#'
    while True:
        nx, ny = move(X, Y, D)
        if out_of_bounds(nx, ny):
            lines[sty][stx] = '.'
            return
        if lines[ny][nx] == '#':
            if ((nx, ny, D) in checked):
                lines[sty][stx] = 'O'
                return
            checked.add((nx, ny, D))
            D = (D+1) % 4
        else:
            X, Y = nx, ny


while True:
    nx, ny = move(x, y, d)
    if out_of_bounds(nx, ny):
        break
    if lines[ny][nx] == '#':
        d = (d+1) % 4
    else:
        if lines[y][x] != 'O' and lines[y][x] != 'X':
            lines[y][x] = 'X'
        check_loop(x, y, d)
        x, y = nx, ny


print("\n".join(["".join(l) for l in lines]))
res = sum([l.count('O') for l in lines])

print("part 2, number of loops: "+str(res))
