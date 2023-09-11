"""
Question: Create a directed graph with K biconnected (beautifully connected) pairs
"Beautifully connected pairs" just means there are at least 2 unique ways to go from node A to B

Constraints on the graph you create: 1 <= V, E <= 5000

My solution: Using triangular numbers
- note: I precomputed all triangular numbers that we need for simplicity, and so we can use binary search

"""

from bisect import bisect_right

# a circular graph (1-2, 2-3, 1-3) with i nodes has tri[i] "beautifully connected pairs"
tri = [0] + [(i * (i + 1)) // 2 for i in range(5001)]

n = int(input())

# first, find the triangular numbers that add up to n
tri_sum = []
prev = 5000
while n > 0:
    rem = bisect_right(tri, n, hi=prev + 1) - 1
    prev = rem
    tri_sum.append(rem)
    n -= tri[rem]

# because a graph with T-1 nodes has tri[T] biconnected pairs, we can create len(tri_sum) separate graphs
# that way, there will be n biconnected pairs in total
edges = []
prev_node = 0
for num in tri_sum:  # for each graph
    edges.append((num + prev_node, 1 + prev_node))  # circular edge that connects start to end

    for i in range(1 + prev_node, num + prev_node):
        edges.append((i, i + 1))

    # connect the current graph to the next as the question requires a connected graph
    # (this won't create any extra biconnected pairs because the graph is directed and this is just one edge)
    # note: we pop the LAST edge appended in this way because it doesn't connect to another graph (∴ is useless)
    edges.append((num + prev_node, num + prev_node + 1))
    prev_node += num

edges.pop()  # remove last edge that is useless
print(prev_node, len(edges))
for i, j in edges:
    print(i, j)
