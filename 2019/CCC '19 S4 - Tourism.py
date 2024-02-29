# WORK IN PROGRESS
# 5/15

n, k = map(int, input().split())
arr = list(map(int, input().split()))

MAX_DAY = (n + k - 1) // k  # "using fewest days possible" means we must use this many days
inf = 1 << 30

# notice that the 2 subtasks don't overlap, this is subtask 1
if 2 * k >= n:
    prefix, suffix, both = [0], [0], [0]
    for i in range(n):
        if i < k and (n - i - 1) < k:
            both.append(arr[i])
        elif i < k:
            prefix.append(arr[i])
        else:
            suffix.append(arr[i])

    both.sort(reverse=True)
    bp = max(prefix)
    bb1 = both[0]
    if len(both) > 1 and k != n:
        bb2 = both[1]
    else:
        bb2 = 0
    bs = max(suffix)

    print(max(bp + bs, bp + bb1, bs + bb1, bb1 + bb2))

