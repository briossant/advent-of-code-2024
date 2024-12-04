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
