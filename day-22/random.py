from libaoc import *

nums = [int(x) for x in readfile()]


def mixAndPrune(secret, x):
    return (secret ^ x) % 16777216


sm = 0
for n in nums:
    for _ in range(2000):
        n = mixAndPrune(n*64, n)
        n = mixAndPrune(n//32, n)
        n = mixAndPrune(n*2048, n)
    print(n)
    sm += n

print("RESuLT:", sm)
