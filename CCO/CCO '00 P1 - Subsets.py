# Graph theory, I guess also dynamic programming because we make sure nothing is calculated more than once
# The graph can have cycles so we use a visited array (watch out for things like A contains A)

# Use a set, don't use a list
# Also use a dict not a defaultdict because keys with empty values are needed

n = int(input())
graph = {}  # a set's subsets
elements = {}  # a set's elements
sets = set()

# construct graph from input
for _ in range(n):
    big, _, small = input().split()
    sets.add(big)

    if big not in elements:  # you have to add the element even if it contains nothing (DO NOT USE DEFAULTDICT)
        elements[big] = set()
    if big not in graph:
        graph[big] = set()

    if small.islower():  # small is an element
        elements[big].add(small)
    else:
        graph[big].add(small)


# fill in the graph with elements using DFS
sets = sorted(list(sets))  # sort lexicographically
for i in sets:
    stack = [i]
    vis = {i}

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if adj in vis:
                continue
            vis.add(adj)

            if adj > i:  # this element was not processed yet, we have to check its subsets
                stack.append(adj)

            # otherwise, we know that we already found all its subsets and can just add them
            for el in elements[adj]:
                elements[i].add(el)  # add all elements from subset

for char in sorted(elements.keys()):
    print(f"{char} = " + "{", end="")
    print(*sorted(list(elements[char])), sep=",", end="")  # print sorted letters
    print("}")
