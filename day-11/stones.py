# f = open("./example.txt", "r")
f = open("./input.txt", "r")
stones = [int(x) for x in f.readline().strip().split(' ')]


def update_stones(stones):
    ln = len(stones)
    for i in range(ln):
        s_x = str(stones[i])
        if stones[i] == 0:
            stones[i] = 1
        elif len(s_x) % 2 == 0:
            stones[i] = int(s_x[0:len(s_x)//2])
            stones.append(int(s_x[len(s_x)//2:]))
        else:
            stones[i] *= 2024


for i in range(25):
    print(i, len(stones))
    update_stones(stones)

print(' '.join([str(x) for x in stones]))
print("number of stones: %d" % len(stones))
