from collections import defaultdict, deque


# check if there is a path from A to B
def bfs(skip):
    visited = set()
    q = deque(["A"])
    while q:
        node = q.popleft()
        if node in visited:
            continue

        visited.add(node)
        if node == "B":
            return True
        for adjacent in graph[node]:
            if (node == skip[0] and adjacent == skip[1]) or (node == skip[1] and adjacent == skip[0]):
                continue
            q.append(adjacent)
    return False


graph = defaultdict(list)
roads = []

r = input()
while r != "**":
    roads.append(r)
    graph[r[0]].append(r[1])
    graph[r[1]].append(r[0])
    r = input()

res = []
for road in roads:
    if not bfs(road):
        res.append(road)

for i in res:
    print(i)
print(f"There are {len(res)} disconnecting roads.")
