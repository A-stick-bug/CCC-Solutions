size = int(input())
trees = int(input())
max = 0

field = [[0 for x in range(size)] for y in range(size)]

for i in range(trees):
    tree = input().split()
    field[int(tree[0])][int(tree[1])] = 1

end = [0,0]

for i in range(size):
    for j in range(size):
        if 1 not in field[]

