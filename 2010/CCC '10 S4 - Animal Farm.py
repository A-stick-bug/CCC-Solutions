# constructing the graph is a large part of the problem
# connection to outside is optional, so we try 2 MST, one with and one without the outside

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


n_nodes = int(input())
edges = {}
inside_edges = []  # edges that connect an area to another
OUTSIDE = n_nodes

for pen in range(n_nodes):
    line = list(map(int, input().split()))
    n = line[0]  # number of points enclosing this area
    line.insert(n + 1, line[1])  # circular, so start connects to end

    for node1 in range(1, n + 1):
        node1, node2, cost = line[node1], line[node1 + 1], line[node1 + n + 1]

        if node1 > node2:  # smaller point first to prevent duplicate edges
            node1, node2 = node2, node1

        edge = (node1, node2, cost)  # (node1, node2, cost)
        if edge in edges:  # if an edge appears twice, it connects 2 areas
            cur = pen
            other = edges[edge]
            if cur > other:  # smaller number goes first
                cur, other = other, cur
            inside_edges.append((cur, other, cost))
            edges.pop(edge)

        else:
            edges[edge] = pen

outside_edges = []
for edge, area in edges.items():  # process edges that connect to outside
    outside_edges.append((area, OUTSIDE, edge[2]))  # (area, outside, cost)

all_edges = inside_edges + outside_edges
inside_edges.sort(key=lambda x: x[2])  # sort by cost
all_edges.sort(key=lambda x: x[2])

# use Kruskal's algorithm to find the minimum spanning tree twice
mst = UnionFind(n_nodes)
mst_size = 0
mst_cost = 0
for node1, node2, cost in inside_edges:
    if mst_size == n_nodes - 1:  # full MST
        break
    if mst.find(node1) != mst.find(node2):
        mst.union(node1, node2)
        mst_cost += cost
        mst_size += 1

if mst_size < (n_nodes - 1):  # wasn't able to connect all nodes
    mst_cost = float('inf')

# check mst with outside
mst2 = UnionFind(n_nodes + 1)
mst_size2 = 0
mst_cost2 = 0
for node1, node2, cost in all_edges:
    if mst_size2 == n_nodes:  # full MST
        break
    if mst2.find(node1) != mst2.find(node2):
        mst2.union(node1, node2)
        mst_cost2 += cost
        mst_size2 += 1

print(min(mst_cost, mst_cost2))
