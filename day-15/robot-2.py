import time

# f = open('./example.txt', 'r')
f = open('./input.txt', 'r')

lines = f.readlines()

Map = []
moves = ""

b = False
for l in lines:
    if l == '\n':
        b = True
    if b:
        moves += l.strip()
    else:
        l = l.replace("#", "##")
        l = l.replace("O", "[]")
        l = l.replace(".", "..")
        l = l.replace("@", "@.")
        Map.append(list(l.strip()))

w = len(Map[0])
h = len(Map)


def robPos(robot):
    for i in range(w):
        for j in range(h):
            if Map[j][i] == '@':
                robot["x"] = i
                robot["y"] = j
                return
    raise Exception("No robots ????")


robot = {"x": 0, "y": 0}
robPos(robot)

dirs = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}


def movesBoxeX(Map, x, y, dx):
    ox = x
    while Map[y][ox] in [']', '[']:
        ox += dx
    if Map[y][ox] == '#':
        return False
    while ox != x:
        Map[y][ox - dx], Map[y][ox] = Map[y][ox], Map[y][ox - dx]
        ox -= dx
    return True


def movesBoxeYaux(Map, x, y, dy, doMove):
    if Map[y][x] != '[':
        raise Exception("Hum this is wrong..")
    oy = y+dy
    if Map[oy][x] == '#' or Map[oy][x+1] == '#':
        return False
    if Map[oy][x] == '.' and Map[oy][x+1] == '.':
        if doMove:
            Map[y][x], Map[oy][x] = Map[oy][x], Map[y][x]
            Map[y][x+1], Map[oy][x+1] = Map[oy][x+1], Map[y][x+1]
        return True
    good = True
    if Map[oy][x] == '[':
        good = movesBoxeYaux(Map, x, oy, dy, doMove)
    elif good:
        if Map[oy][x] == ']':
            good = movesBoxeYaux(Map, x-1, oy, dy, doMove)
        if good and Map[y+dy][x+1] == '[':
            good = movesBoxeYaux(Map, x+1, oy, dy, doMove)
    if not good:
        return False
    if doMove:
        Map[y][x], Map[oy][x] = Map[oy][x], Map[y][x]
        Map[y][x+1], Map[oy][x+1] = Map[oy][x+1], Map[y][x+1]
    return True


def movesBoxeY(Map, x, y, dy):
    if Map[y][x] == '#':
        return False
    if Map[y][x] == '.':
        return True
    res = False
    if Map[y][x] == ']':
        res = movesBoxeYaux(Map, x-1, y, dy, False)
    else:
        res = movesBoxeYaux(Map, x, y, dy, False)
    if res:
        if Map[y][x] == ']':
            movesBoxeYaux(Map, x-1, y, dy, True)
        else:
            movesBoxeYaux(Map, x, y, dy, True)
    return res


def MovRobot(robot, Map, dx, dy):
    nx, ny = robot["x"] + dx, robot["y"] + dy  # next robot pos
    ox, oy = nx, ny  # next obstacle pos
    if dy == 0:
        if not movesBoxeX(Map, ox, oy, dx):
            return False
    else:
        if not movesBoxeY(Map, ox, oy, dy):
            return False
    Map[robot["y"]][robot["x"]] = '.'
    robot["x"] = nx
    robot["y"] = ny
    Map[ny][nx] = '@'
    return True


print('\n'.join([''.join(l) for l in Map]))

for m in moves:
    time.sleep(0.0002)
    dx, dy = dirs[m]
    if not MovRobot(robot, Map, dx, dy):
        print("==== " + m + " ---- STUCK ")
    else:
        print("==== " + m)

    print('\n'.join([''.join(l) for l in Map]))


res = sum([sum([100 * y + x if Map[y][x] == '[' else 0 for x in range(w)])
          for y in range(h)])

print("result: " + str(res))
