# Kahn's algorithm for topological sorting
# using heapq to ensure that the smallest number task is outputted first

import heapq

reqs = [999, 1, 0, 0, 2, 1, 0, 1]  # in-degree, 0 is not a valid task number, it's just there for 1-indexing
graph = {  # original list
    1: [4, 7],
    2: [1],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: []
}

while True:  # taking inputs
    before = int(input())
    after = int(input())
    if before == 0:
        break
    reqs[after] += 1
    graph[before].append(after)

pq = []  # start with tasks without reqs
for i, val in enumerate(reqs):
    if val == 0:
        pq.append(i)

# a priority queue is used to ensure that the smallest number task is always done first
# the problem is possible with a regular queue but is slightly more complicated (and probably less intuitive)
heapq.heapify(pq)

order = []
while pq:
    task = heapq.heappop(pq)
    order.append(task)

    for adj in graph[task]:
        reqs[adj] -= 1
        if reqs[adj] == 0:
            heapq.heappush(pq, adj)

if len(order) == 7:
    print(*order)
else:  # some tasks couldn't be completed
    print("Cannot complete these tasks. Going to bed.")
