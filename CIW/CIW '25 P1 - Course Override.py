# https://dmoj.ca/problem/ciw25p1
# Bitmask optimizations + check if 2 axis-aligned rectangles overlap
# TC: O(n * 2^n)

def overlap(r1, r2):
    def suboverlap(r1, r2):  # check 4 corners
        x = [r1[0], r1[1]]
        y = [r1[2], r1[3]]
        for x1 in x:
            for y1 in y:
                if r2[0] <= x1 <= r2[1] and r2[2] <= y1 <= r2[3]:
                    return True
        # edge case
        if (r2[0] <= r1[0] <= r1[1] <= r2[1]) and (r1[2] <= r2[2] <= r2[3] <= r1[3]):
            return True
        return False

    return suboverlap(r1, r2) or suboverlap(r2, r1)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# simplify v to total value
for i in range(n):
    arr[i][5] *= (arr[i][1] - arr[i][0] + 1) * (arr[i][3] - arr[i][2] + 1)

mandatory = 0
for i in range(n):
    if arr[i][4]:
        mandatory |= 1 << i

conflict = [0] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if overlap(arr[i], arr[j]):
            conflict[i] |= 1 << j

best = -1
for mask in range(1 << n):  # try all combinations
    if mask.bit_count() < m or mask | mandatory != mask:
        continue

    works = True
    for i in range(n):  # ensure no conflicts
        if mask & (1 << i) and conflict[i] & mask != 0:
            works = False
            break

    if works:
        best = max(best, sum(arr[i][5] for i in range(n) if mask & (1 << i)))

print(best)
