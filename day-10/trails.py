# f = open('./example.txt', 'r')
f = open('./input.txt', 'r')

lines = f.readlines()
trails = [list(l.strip()) for l in lines]
w = len(trails[0])
h = len(trails)


def cpy(l):
    return [[x for x in y] for y in l]


def trailhead_score(tr_l, x, y):
    if tr_l[y][x] == '9':
        tr_l[y][x] = '#'
        return
    tr_next = str(int(tr_l[y][x]) + 1)
    if x > 0 and tr_l[y][x-1] == tr_next:
        trailhead_score(tr_l, x-1, y)
    if y > 0 and tr_l[y-1][x] == tr_next:
        trailhead_score(tr_l, x, y-1)
    if x < w-1 and tr_l[y][x+1] == tr_next:
        trailhead_score(tr_l, x+1, y)
    if y < h-1 and tr_l[y+1][x] == tr_next:
        trailhead_score(tr_l, x, y+1)


res = 0
for y in range(h):
    for x in range(w):
        if trails[y][x] == '0':
            tr_l = cpy(trails)
            trailhead_score(tr_l, x, y)
            print('\n'.join([''.join(l) for l in tr_l]))
            tr_score = sum([l.count('#') for l in tr_l])
            print(tr_score)
            res += tr_score

print("trails found: " + str(res))
