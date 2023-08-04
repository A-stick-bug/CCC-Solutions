# because the distance between 2 intersections must not be more than the current
# we can remove an edge and if it doesn't affect the shortest distance between points
# start doing this from the costly edges to save the most money


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
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


n_nodes, n_edges = map(int, input().split())
edges = []
for _ in range(n_edges):
    edges.append(list(map(int, input().split())))
edges.sort(key=lambda x: x[3], reverse=True)

mst = UnionFind(n_nodes + 1)
mst_edges = 0
cost = 0
for a, b, _, c in edges:
    if mst_edges == n_nodes - 1:  # full mst
        break
    if mst.find(a) != mst.find(b):  # add edge
        cost += c
        mst.union(a, b)
        mst_edges += 1

print(cost)
