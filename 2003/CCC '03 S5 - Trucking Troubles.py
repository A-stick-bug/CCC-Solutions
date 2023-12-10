# might take some time to realize but this question is basically Kruskal's Algorithm
# finding the minimum spanning tree will let you go to all destinations (time doesn't matter)
# also sort with max edges first because we want a 'maximum spanning tree' that allows most weight

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.rank[rx] > self.rank[ry]:
                self.root[ry] = rx
            elif self.rank[rx] < self.rank[ry]:
                self.root[rx] = ry
            else:
                self.root[ry] = rx
                self.rank[rx] += 1


n_cities, n_roads, n_dest = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(n_roads)]
destinations = {int(input()) for _ in range(n_dest)}
destinations.add(1)  # starting point is also in MST

roads.sort(reverse=True, key=lambda x: x[2])  # sort by weight descending, looking for maximum weight limit
mst = UnionFind(n_cities + 1)

res = float('inf')
for start, end, weight in roads:
    if not destinations:  # we don't need all the edges inside our mst, only the destinations
        break
    if mst.find(start) != mst.find(end):  # does not create a cycle
        mst.union(start, end)
        res = min(res, weight)

        if mst.find(start) == mst.find(1):
            destinations.discard(start)
        if mst.find(end) == mst.find(1):
            destinations.discard(end)

print(res)
