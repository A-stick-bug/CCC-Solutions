def bfs(graph, start, end):
    queue = [start]
    visited = set()
    distance = {start: 0}

    while queue:
        node = queue.pop(0)
        if node == end:
            return distance[node]

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                if neighbor in distance.keys():
                    distance[neighbor] = min(distance[node] + 1, distance[neighbor])
                else:
                    distance[neighbor] = distance[node] + 1

    return "Not connected"


graph = {
    1: [6],
    2: [6],
    3: [4, 5, 6, 15],
    4: [3, 5, 6],
    5: [3, 4, 6],
    6: [1, 2, 3, 4, 5, 7],
    7: [6, 8],
    8: [7, 9],
    9: [8, 10, 12],
    10: [9, 11],
    11: [10, 12],
    12: [9, 11, 13],
    13: [12, 14, 15],
    14: [13],
    15: [3, 13],
    16: [17, 18],
    17: [16, 18],
    18: [16, 17],
}

command = input()
while command != "q":
    if command == "i":
        x = int(input())
        y = int(input())
        if x not in graph.keys():
            graph[x] = []
        if y not in graph.keys():
            graph[y] = []

        if y not in graph[x]:
            graph[x].append(y)
            graph[y].append(x)

    elif command == "d":
        x = int(input())
        y = int(input())
        graph[x].remove(y)
        graph[y].remove(x)

    elif command == "n":
        x = int(input())
        print(len(graph[x]))

    elif command == "f":
        x = int(input())
        to_remove = len(graph[x]) + 1
        total = set(graph[x])
        total.add(x)
        for friend in graph[x]:
            for friend_friend in graph[friend]:
                total.add(friend_friend)
        print(len(total) - to_remove)

    elif command == "s":
        x = int(input())
        y = int(input())
        print(bfs(graph,x,y))

    command = input()

