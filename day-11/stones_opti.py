# f = open("./example.txt", "r")
f = open("./input.txt", "r")
stones = [(1, int(x)) for x in f.readline().strip().split(' ')]

SMALL_STONE_MAX = 100000
small_stones = [0 for _ in range(SMALL_STONE_MAX)]

for n in stones:
    if n[1] < SMALL_STONE_MAX:
        small_stones[n[1]] += n[0]

stones = list(filter(lambda x: x[1] >= SMALL_STONE_MAX, stones))


def update_small_stones(small_stones):
    l = [0 for _ in range(SMALL_STONE_MAX)]
    l[1] = small_stones[0]
    for i in range(1, SMALL_STONE_MAX):
        s_x = str(i)
        if len(s_x) % 2 == 0:
            sl = int(s_x[0:len(s_x)//2])
            sr = int(s_x[len(s_x)//2:])
            l[sl] += small_stones[i]
            l[sr] += small_stones[i]
        else:
            n = i * 2024
            if n < SMALL_STONE_MAX:
                l[n] += small_stones[i]
            else:
                stones.append((small_stones[i], n))
    return l


def update_stones(stones):
    ln = len(stones)
    l = [0 for _ in range(SMALL_STONE_MAX)]
    for i in range(ln):
        (count, n) = stones[i]
        s_x = str(n)
        if len(s_x) % 2 == 0:
            sl = int(s_x[0:len(s_x)//2])
            sr = int(s_x[len(s_x)//2:])
            if sl < SMALL_STONE_MAX and sr < SMALL_STONE_MAX:
                l[sl] += count
                l[sr] += count
                stones[i] = (0, 0)
            elif sl < SMALL_STONE_MAX:
                stones[i] = (count, sr)
                l[sl] += count
            elif sr < SMALL_STONE_MAX:
                stones[i] = (count, sl)
                l[sr] += count
            else:
                stones[i] = (count, sr)
                stones.append((count, sl))
        else:
            stones[i] = (count, n*2024)
    return l


for i in range(75):
    print(i, len(stones))
    l1 = update_stones(stones)
    l2 = update_small_stones(small_stones)
    stones = list(filter(lambda x: x[0] > 0, stones))
    small_stones = [x+y for x, y in zip(l1, l2)]


res = sum(small_stones)
res += sum([c for (c, _) in stones])

print("number of stones: %d" % res)
