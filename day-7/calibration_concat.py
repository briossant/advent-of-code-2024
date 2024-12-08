f = open('./input.txt', 'r')
lines = [l.split(':') for l in f.readlines()]

results = [int(l[0]) for l in lines]
operands_list = [[int(x) for x in l[1].strip().split(' ')] for l in lines]


def calculate(result, operands, acc):
    if operands == []:
        return result == acc
    acc1 = acc + operands[0]
    acc2 = acc * operands[0]
    acc3 = int(str(acc) + str(operands[0]))
    return (calculate(result, operands[1:], acc1)
            or calculate(result, operands[1:], acc2)
            or calculate(result, operands[1:], acc3))


res = 0
for i in range(len(results)):
    if calculate(results[i], operands_list[i][1:], operands_list[i][0]):
        res += results[i]

print("part 2: " + str(res))
