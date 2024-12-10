# f = open('./example.txt', 'r')
f = open('./input.txt', 'r')

lines = f.readlines()
trails = [list(l.strip()) for l in lines]
w = len(trails[0])
h = len(trails)


def trailhead_score(tr_l, x, y):
    if tr_l[y][x] == '9':
        return 1
    tr_next = str(int(tr_l[y][x]) + 1)
    sm = 0
    if x > 0 and tr_l[y][x-1] == tr_next:
        sm += trailhead_score(tr_l, x-1, y)
    if y > 0 and tr_l[y-1][x] == tr_next:
        sm += trailhead_score(tr_l, x, y-1)
    if x < w-1 and tr_l[y][x+1] == tr_next:
        sm += trailhead_score(tr_l, x+1, y)
    if y < h-1 and tr_l[y+1][x] == tr_next:
        sm += trailhead_score(tr_l, x, y+1)
    return sm


res = 0
for y in range(h):
    for x in range(w):
        if trails[y][x] == '0':
            res += trailhead_score(trails, x, y)

print("trails found: " + str(res))
