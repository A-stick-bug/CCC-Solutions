# https://dmoj.ca/problem/ccc24s3
# credit to yujhtheyujh for ideas and sharing his clever way of thinking
# consider this question to be crossing lines between the 2 lists without intersecting any
#
# observations: left and right swipes NEVER overlap
# note to self: add proper explanation and simplify solution later

n = int(input())
arr = list(map(int, input().split()))
target = list(map(int, input().split()))

swipes_l = []
swipes_r = []

j = 0  # index in target
for i in range(n):
    left = [j, i]  # try swiping left
    sl = False  # check if we moved this turn
    while j < i and target[j] == arr[i]:
        j += 1
        sl = True
    if sl:
        swipes_l.append(left.copy())

    right = [i, -1]  # try swiping right
    sr = False
    while j < n and target[j] == arr[i]:
        right[1] = j
        j += 1
        sr = True
    if sr and right[0] != right[1]:
        swipes_r.append(right.copy())

if j == n:
    print("YES")

    # output in correct order, that's the annoying part of this method
    print(len(swipes_l) + len(swipes_r))
    swipes_r.sort(key=lambda x: x[1], reverse=True)
    swipes_l.sort(key=lambda x: x[0])
    for i in swipes_r:
        print("R", i[0], i[1])
    for i in swipes_l:
        print("L", i[0], i[1])

else:
    print("NO")

"""
1 3 3 2 1
1 1 2 1 1
"""
