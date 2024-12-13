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


def move(x, y):
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


while True:
    nx, ny = move(x, y)
    if out_of_bounds(nx, ny):
        break
    if lines[ny][nx] == '#':
        d = (d+1) % 4
    else:
        x, y = nx, ny
        lines[y][x] = 'X'

res = sum([l.count('X') for l in lines])

print("part 1: "+str(res))
