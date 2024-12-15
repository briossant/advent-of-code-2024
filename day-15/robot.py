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


def MovRobot(robot, Map, dx, dy):
    nx, ny = robot["x"] + dx, robot["y"] + dy  # next robot pos
    ox, oy = nx, ny  # next obstacle pos
    while Map[oy][ox] == 'O':
        ox += dx
        oy += dy
    if Map[oy][ox] == '#':
        return  # can't move

    Map[ny][nx], Map[oy][ox] = Map[oy][ox], Map[ny][nx]
    robot["x"] = nx
    robot["y"] = ny


print('\n'.join([''.join(l) for l in Map]))

for m in moves:
    dx, dy = dirs[m]
    MovRobot(robot, Map, dx, dy)


print('\n'.join([''.join(l) for l in Map]))


res = sum([sum([100 * y + x if Map[y][x] == 'O' else 0 for x in range(w)])
          for y in range(h)])

print("result: " + str(res))
