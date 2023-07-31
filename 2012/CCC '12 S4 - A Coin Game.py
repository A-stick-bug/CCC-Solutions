# 15/15
# Passes all test cases, including ones from the senior division
# uses bidirectional BFS to speed things up

from collections import deque


def store(coins):
    return "".join(map(str, coins))


def get_neighbors(config):
    neighbors = []
    for i in range(n):
        if not config[i]:  # nothing to move from here
            continue

        if i != 0 and (not config[i - 1] or config[i][-1] < config[i - 1][-1]):  # try moving left
            new_config = [i.copy() for i in config]
            to_move = new_config[i].pop()
            new_config[i - 1].append(to_move)  # move coin to the left
            neighbors.append(new_config)

        if i != n - 1 and (not config[i + 1] or config[i][-1] < config[i + 1][-1]):  # try moving right
            new_config = [i.copy() for i in config]
            to_move = new_config[i].pop()
            new_config[i + 1].append(to_move)  # move coin to the right
            neighbors.append(new_config)
    return neighbors


# for each test case
while True:
    n = int(input())
    if n == 0:
        break

    coins = list(map(int, input().split()))
    coins = [[i] for i in coins]  # each element is a stack of coins
    end = [[i] for i in range(1, n + 1)]  # the state we are trying to reach

    q_start = deque()
    q_start.append(coins)
    used_start = {store(coins): 0}

    q_end = deque()
    q_end.append(end)
    used_end = {store(end): 0}

    found = False
    while q_start and q_end:
        config = q_start.popleft()
        c = store(config)
        steps = used_start[c]

        if c in used_end:
            print(steps + used_end[c])
            found = True
            break

        for neighbor in get_neighbors(config):
            temp = store(neighbor)
            if temp not in used_start:
                q_start.append(neighbor)
                used_start[temp] = steps + 1

        # do same thing for end
        config = q_end.popleft()
        c = store(config)
        steps = used_end[c]

        if c in used_start:
            print(steps + used_start[c])
            found = True
            break

        for neighbor in get_neighbors(config):
            temp = store(neighbor)
            if temp not in used_end:
                q_end.append(neighbor)
                used_end[temp] = steps + 1

    if not found:
        print("IMPOSSIBLE")


# # brute force through all combinations
# # passes the test cases for junior division
# # TLE on senior division, check the c++ version of this code for a solution that passes
#
# from collections import deque
#
# # for each test case
# while True:
#     n = int(input())
#     if n == 0:
#         break
#
#     coins = list(map(int, input().split()))
#     coins = [[i] for i in coins]  # each element is a stack of coins
#     end = [[i] for i in range(1, n+1)]  # the state we are trying to reach
#     store = lambda coins: "".join(map(str, coins))  # save space when storing in used
#
#     q = deque()
#     q.append((coins, 0))
#     used = set()
#     used.add(store(coins))
#
#     found = False
#     while q:
#         config, steps = q.popleft()
#         # print(config)
#
#         if config == end:  # is sorted
#             print(steps)
#             found = True
#
#         for i in range(n):
#             if not config[i]:  # nothing to move from here
#                 continue
#
#             if i != 0 and (not config[i - 1] or config[i][-1] < config[i - 1][-1]):  # try moving left
#                 new_config = [i.copy() for i in config]
#                 to_move = new_config[i].pop()
#                 new_config[i - 1].append(to_move)  # move coin to the left
#
#                 temp = store(new_config)
#                 if temp not in used:
#                     q.append((new_config, steps + 1))
#                     used.add(temp)
#
#             if i != n - 1 and (not config[i + 1] or config[i][-1] < config[i + 1][-1]):  # try moving right
#                 new_config = [i.copy() for i in config]
#                 to_move = new_config[i].pop()
#                 new_config[i + 1].append(to_move)  # move coin to the right
#
#                 temp = store(new_config)
#                 if temp not in used:
#                     q.append((new_config, steps + 1))
#                     used.add(temp)
#
#     if not found:
#         print("IMPOSSIBLE")
