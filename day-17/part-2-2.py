from libaoc import *

lines = readfile()

# ordre de grandeur de regA - pas de bruteforce possible;
# iregA = 100000000000000
iregA = 0
iregB = findNums(lines[1])[0]
iregC = findNums(lines[2])[0]

program = findNums(lines[4])


def runProgram(regA, regB):
    i = 0
    while True:
        regB = (regA % 8) ^ 1
        regB = (regB ^ (regA // pow(2, regB))) ^ 4
        regA //= 8
        if regB % 8 != program[i]:
            return False
        i += 1
        if regA == 0:
            return i == len(program)


regAmin = 1
regAmax = 7
for i in range(1, len(program)):
    regAmin *= 8
    regAmax *= 8 + 7

print(regAmin)
print(regAmax)

regA = [0]
for i in range(len(program)-1, -1, -1):
    to_rm = []
    for x in range(len(regA)):
        regA[x] *= 8
        good = False
        for j in range(0, 8):
            nA = regA[x] + j
            regB = (nA % 8) ^ 1
            regB = (regB ^ (nA // pow(2, regB))) ^ 4
            if regB % 8 == program[i]:
                if not good:
                    regA[x] += j
                    good = True
                else:
                    regA.append(regA[x] + j)
        if not good:
            to_rm.append(x)
    print(', '.join([str(x) for x in regA]))
    to_rm.reverse()
    for x in to_rm:
        regA.pop(x)

print(regA)
for rA in regA:
    print(rA, runProgram(rA, 0))

exit(0)
iregA = regAmin
while not runProgram(iregA, iregB):
    if iregA % 10000 == 0:
        print(iregA)
    iregA += 1


print(iregA-1)
