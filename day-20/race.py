from libaoc import *

Map = MapLoad()

w, h = len(Map[0]), len(Map)

BFS2(Map, 'S', 'E')

shortcut = {}
ttshortcuts = 0
for x in range(1, w-1):
    for y in range(1, h-1):
        if Map[y][x] == '#':
            continue

        for dx, dy in cross_dirs:
            nx, ny = x+dx, y+dy
            if Map[ny][nx] != '#':
                continue
            nx, ny = nx+dx, ny+dy
            if MapIsOutOfBounds(Map, nx, ny) or Map[ny][nx] == '#':
                continue
            diff = Map[ny][nx] - Map[y][x] - 2
            if diff >= 0:
                if diff in shortcut:
                    shortcut[diff] += 1
                else:
                    shortcut[diff] = 1
            if diff >= 100:
                ttshortcuts += 1

print(shortcut)
print("shortcuts:", ttshortcuts)
