import sys


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


n, m, d = map(int, input().split())
edges = []
current = []  # the current plan
for i in range(m):
    pipe = tuple(map(int, input().split()))
    if i < n - 1:
        current.append(pipe)
    edges.append(pipe)

edges.sort(key=lambda x: x[2])  # sort by cost
uf = UnionFind(n + 1)
mst = []

for n1, n2, cost in edges:
    if len(mst) == n - 1:  # full mst
        break
    if uf.find(n1) != uf.find(n2):
        uf.union(n1, n2)
        mst.append((n1, n2, cost))

mst_set, original_set = set(mst), set(current)
no_pipe = len(mst_set - original_set)  # time it takes, assuming no pipe usage
if d == 0:  # no pipe enhancer
    print(no_pipe)
    sys.exit()

# make a second MST but considering the pipe enhancer
mst_max_cost = mst[-1][2]  # highest cost in the mst without pipe enhancer
uf = UnionFind(n + 1)  # reset variables
mst = []

for n1, n2, cost in edges:
    if len(mst) == n - 1:  # full mst
        break
    if uf.find(n1) != uf.find(n2):
        # if the cost is less than previous max, it must be in the mst (or else it's not a mst)
        # also keep it if it's part of the original plan (because you don't need to spend time changing it to a new one)
        if cost < mst_max_cost or (cost == mst_max_cost and (n1, n2, cost) in original_set):
            uf.union(n1, n2)
            mst.append((n1, n2, cost))

        # if there is a pipe in the original plan that can be zeroed by enhancer,
        # we can now put it in the MST and save a day
        elif cost <= d and (n1, n2, cost) in original_set:
            print(no_pipe - 1)
            sys.exit()

print(no_pipe)  # if we got here, we couldn't take advantage of the pipe enhancer
