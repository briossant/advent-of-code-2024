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


def check_loop(X, Y, D):
    loop = False
    to_add = []
    nd = (D+1) % 4
    stx, sty = move(X, Y, D)

    if lines[sty][stx].count('#'):
        raise ValueError('Non non')
    if lines[sty][stx] == 'O':
        return

    lines[sty][stx] = '#' + str(D)
    while True:
        nx, ny = move(X, Y, nd)
        if out_of_bounds(nx, ny):
            break
        if lines[ny][nx].count('#'):
            if lines[ny][nx].count(str(nd)) or [nx, ny, nd] in to_add:
                print(stx, sty, D)
                loop = True
                break
            to_add.append([nx, ny, nd])
            nd = (nd+1) % 4
        else:
            X, Y = nx, ny
    lines[sty][stx] = 'O' if loop else '.'


c = ['^', '>', 'v', '<']
while True:
    nx, ny = move(x, y, d)
    if out_of_bounds(nx, ny):
        break
    if lines[ny][nx].count('#'):
        lines[ny][nx] += str(d)
        d = (d+1) % 4
    else:
        if lines[y][x] != 'O':
            lines[y][x] = c[d]
        check_loop(x, y, d)
        x, y = nx, ny


def rep(x):
    if x.count('#'):
        return '#'
    return x


print("\n".join(["".join(map(rep, l)) for l in lines]))
res = sum([l.count('O') for l in lines])

print("part 2, number of loops: "+str(res))
