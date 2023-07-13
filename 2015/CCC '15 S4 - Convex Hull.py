import sys
import heapq

input = sys.stdin.readline
hull, n_islands, n_routes = map(int, input().split())
graph = [[] for _ in range(n_islands + 1)]

for _ in range(n_routes):
    a, b, pt, dmg = map(int, input().split())
    graph[a].append((b, pt, dmg))
    graph[b].append((a, pt, dmg))
start, end = map(int, input().split())

inf = 10 ** 9 + 1
dist = [[inf, inf] for _ in range(n_islands + 1)]
dist[start] = (0, 0)
pq = [(0, start, 0)]

while pq:
    time, island, damage = heapq.heappop(pq)
    if island == end:
        print(time)
        sys.exit()

    if time > dist[island][0] and damage > dist[island][1]:
        continue

    for adj, adj_time, adj_damage in graph[island]:
        new_time = time + adj_time
        new_damage = damage + adj_damage

        if new_damage >= hull:  # broken hull, can't take this path
            continue

        if new_time < dist[adj][0] or new_damage < dist[adj][1]:
            dist[adj][0] = new_time
            dist[adj][1] = new_damage
            heapq.heappush(pq, (new_time, adj, new_damage))

print(-1)


# similar alternate solution
# import heapq
# import sys
# from collections import defaultdict
#
# hull, n_islands, n_routes = map(int, input().split())
#
# # inside each defaultdict, the key is the destination node and the value is all the paths
# graph = [defaultdict(list) for n in range(n_islands + 1)]
# for m in range(n_routes):
#     a, b, time, damage = map(int, input().split())
#     graph[a][b].append((time, damage))
#     graph[b][a].append((time, damage))
#
# inf = 10**9 + 1
#
# start, end = map(int, input().split())
#
# min_time = inf
# distance = [[inf for _ in range(201)] for _ in range(n_islands+1)]
#
# for i in range(201):
#     distance[start][i] = 0
#
# pq = [(0, start, hull)]
#
# visited = set()
# while pq:
#     cost, island, hp = heapq.heappop(pq)
#
#     if island == end:  # end reached
#         print(cost)
#         sys.exit()
#
#     if (island,hp) in visited:
#         continue
#     visited.add((island,hp))
#
#     for adj in graph[island]:  # for every island we can reach from teh current
#         for adj_time, adj_damage in graph[island][adj]:  # process every route
#             new_time = distance[island][hp] + adj_time
#             new_hp = hp - adj_damage
#
#             if new_hp > 0:
#                 if new_time < distance[adj][new_hp]:
#                     distance[adj][new_hp] = new_time
#                 heapq.heappush(pq, (new_time, adj, new_hp))
#
# print(-1)  # can't get to end
