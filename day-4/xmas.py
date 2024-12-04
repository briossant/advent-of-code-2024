f = open('./input.txt', 'r')
# f = open('./example.txt', 'r')

lines = f.readlines()
lines = [l.strip() for l in lines]
h = len(lines)
w = len(lines[0])


def find_word_at(word, x, y):
    diagl, diagr, right, down = 1, 1, 1, 1
    for i in range(len(word)):
        if x+i >= w or lines[y][x+i] != word[i]:
            right = 0
        if y+i >= h or lines[y+i][x] != word[i]:
            down = 0
        if y+i >= h or x+i >= w or lines[y+i][x+i] != word[i]:
            diagr = 0
        if y+i >= h or x-i < 0 or lines[y+i][x-i] != word[i]:
            diagl = 0
    return diagl + diagr + right + down


word = ['X', 'M', 'A', 'S']
XMAS = [[find_word_at(word, x, y) for x in range(w)] for y in range(h)]

word.reverse()
XMAS = [[XMAS[y][x] + find_word_at(word, x, y)
         for x in range(w)] for y in range(h)]

total = sum([sum(l) for l in XMAS])

print("numbre of XMAS: " + str(total))

# part 2

word = ['M', 'M', 'S', 'S']


def find_x_mas(x, y):
    if lines[y][x] != 'A':
        return 0
    t = [lines[y-1][x-1], lines[y+1][x-1], lines[y-1][x+1], lines[y+1][x+1]]
    if t[0] == t[3]:
        return 0
    t.sort()
    return all(x == y for x, y in zip(t, word))


XMAS = [[find_x_mas(x, y) for x in range(1, w-1)] for y in range(1, h-1)]

total = sum([sum(l) for l in XMAS])

print("numbre of X-MAS: " + str(total))
