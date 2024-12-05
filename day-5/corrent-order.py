f = open('./input.txt', 'r')
# f = open('./example.txt', 'r')

lines = f.readlines()
orders = [[False for _ in range(100)] for _ in range(100)]

l1 = lines[:lines.index('\n')]
l2 = lines[lines.index('\n')+1:]

l1 = [l.strip().split('|') for l in l1]
for l in l1:
    orders[int(l[0])][int(l[1])] = True


def check_order(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if not orders[l[i]][l[j]]:
                return 0
    return l[len(l)//2]


l2 = [[int(x) for x in l.strip().split(',')] for l in l2]

is_ordered = [check_order(l) for l in l2]

print("part 1: " + str(sum(is_ordered)))


def fix_order(l):
    for i in range(len(l)):
        for j in range(0, i):
            if orders[l[i]][l[j]]:
                l[i], l[j] = l[j], l[i]
    return l[len(l)//2]


fixed_orders = [0 if is_ordered[i] > 0 else fix_order(l2[i]) for i in
                range(len(l2))]

print("part 2: " + str(sum(fixed_orders)))
