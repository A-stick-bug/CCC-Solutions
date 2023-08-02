# simple graph theory with DFS to detect cycle and keeping track of distance
# since each student is assigned exactly one friend,
# we just need a (node, distance) tuple that represents the next element to process

n = int(input())  # taking input
graph = [None for _ in range(10000)]  # the i-th element is the person that 'i' is assigned to
for _ in range(n):
    a, b = map(int, input().split())
    graph[a] = b


def separation(start, end):
    node = (start, 0)  # each node only points to one element, so we don't even need a stack/queue
    while True:
        node, distance = node  # unpack for convenience
        if node == end:
            return distance

        # if came back to start and didn't reach our destination, it is not in this circle
        elif node == start and distance != 0:
            return -1

        node = (graph[node], distance + 1)


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    sep = separation(a, b)
    if sep == -1:  # not part of this circle
        print("No")
    else:
        print(f"Yes {sep - 1}")  # minus one because 2 adjacent nodes is 0 separation
