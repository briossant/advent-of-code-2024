from libaoc import *
from pprint import pprint

nums = [int(x) for x in readfile()]


def mixAndPrune(secret, x):
    return (secret ^ x) % 16777216


def update(n):
    n = mixAndPrune(n*64, n)
    n = mixAndPrune(n//32, n)
    n = mixAndPrune(n*2048, n)
    return n


ct = {}

sm = 0
i = 0
for n in nums:
    i += 1
    print(i, len(nums))
    ct2 = {}
    p1, p2, p3 = 0, 0, 0
    last = n % 10
    n = update(n)
    p1 = n % 10 - last
    last, n = n % 10, update(n)
    p2 = n % 10 - last
    last, n = n % 10, update(n)
    p3 = n % 10 - last
    for _ in range(2000-3):
        last, n = n % 10, update(n)
        key = (p1, p2, p3, n % 10 - last)
        if key not in ct2:
            ct2[key] = 42
            if key in ct:
                ct[key] += n % 10
            else:
                ct[key] = n % 10
        p1, p2, p3 = p2, p3, n % 10-last
    sm += n

print("sum:", sm)

# pprint(ct)

res = max(ct.values())
print("RESULT:", res)
