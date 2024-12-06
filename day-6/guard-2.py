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
        break


d = 0
c = ['^', '>', 'v', '<']


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


loops = 0
while True:
    nx, ny = move(x, y, d)
    nd = (d+1) % 4
    if out_of_bounds(nx, ny):
        break
    if lines[ny][nx].count('#'):
        lines[ny][nx] += str(d)
        d = nd
    else:
        x, y = nx, ny
        to_add = []
        while True:
            nnx, nny = move(nx, ny, nd)
            if out_of_bounds(nnx, nny):
                nx, ny = nnx, nny
                break
            if lines[nny][nnx].count('#'):
                if lines[nny][nnx].count(str(nd)) or [nnx, nny, nd] in to_add:
                    loops += 1
                    break
                to_add.append([nnx, nny, nd])
                nd = (nd+1) % 4
            else:
                nx, ny = nnx, nny
        if not out_of_bounds(nx, ny):
            lines[y][x] = 'O'
            for rx, ry, rd in to_add:
                lines[ry][rx] += str(rd)

print("\n".join(["".join(l) for l in lines]))
print("part 2, number of loops: "+str(loops))
