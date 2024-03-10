"""
https://dmoj.ca/problem/ccc24s3
credit to yujhtheyujh for ideas and sharing his clever way of thinking
consider this question to be crossing lines between the 2 lists without intersecting any

observations:
- left and right swipes NEVER overlap
- right swipes must be output in reversed order to prevent overriding values
  - other than this, the order of swipes doesn't matter
"""

n = int(input())
arr = input().split()
target = input().split()

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
    print(len(swipes_l) + len(swipes_r))
    for i in reversed(swipes_r):  # output right swipes in reverse order to prevent overriding values
        print("R", i[0], i[1])
    for i in swipes_l:
        print("L", i[0], i[1])

else:
    print("NO")

"""
5
1 3 3 2 1
1 1 2 1 1

YES
3
R 0 1
L 2 3
L 3 4
"""
