f = open("./input-treated.txt", "r")
l = f.readlines()
l = [x.strip().split(' ') for x in l]

res = sum([int(x[0]) * int(x[1]) if len(x) > 1 else 0 for x in l])
print("part 1: " + str(res))

res = 0
do = True
for x in l:
    if len(x) == 1:
        do = len(x[0]) == 4  # len("do()") = 4 ; len("don't()") = 6
    elif do:
        res += int(x[0]) * int(x[1])

print("part 1: " + str(res))
