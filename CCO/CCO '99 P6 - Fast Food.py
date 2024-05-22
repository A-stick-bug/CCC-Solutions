# https://dmoj.ca/problem/cco99p6
# similar idea as https://dmoj.ca/problem/ccc10s3
# Binary search + greedy
# Greedy idea: go left to right, if the current house is not within _dist_ of a warehouse,
#              create a warehouse at the rightmost position such that the current house
#              is within _dist_ of it

def find_placements(dist):
    """determine if it is possible to place k warehouses for a max distance of <= _dist_
       if so, return the placements of the warehouses"""
    covers = -10000000000  # everything up to here is at most _dist_ from a warehouse
    used = 0
    placements = []
    for i, loc in enumerate(locs):
        if loc > covers:
            # greedily find best placement (make it the farthest)
            j = i
            while j + 1 < n and locs[j + 1] - loc <= dist:
                j += 1
            if used == k:
                return [-1]  # no valid placements
            covers = locs[j] + dist  # place warehouse at locs[j]
            used += 1
            placements.append(locs[j])

    # corner case: we need to place exactly K warehouses and we placed less
    placements = placements + [placements[-1]]*(k-len(placements))
    return placements


while True:
    n = int(input())
    if n == 0:
        break

    k = int(input())
    locs = [int(input()) for _ in range(n)]

    low = 0
    high = 1_000_000_000  # template binary search
    while low <= high:
        mid = (low + high) // 2
        if find_placements(mid) != [-1]:
            high = mid - 1
        else:
            low = mid + 1

    print(*find_placements(low))
    print(low)
