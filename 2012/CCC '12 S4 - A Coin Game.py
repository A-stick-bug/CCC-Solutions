# brute force through all combinations
# passes the test cases for junior division
# TLE on senior division, check the c++ version of this code for a solution that passes

from collections import deque

# for each test case
while True:
    n = int(input())
    if n == 0:
        break

    coins = list(map(int, input().split()))
    coins = [[i] for i in coins]  # each element is a stack of coins
    end = [[i] for i in range(1, n+1)]  # the state we are trying to reach
    store = lambda coins: "".join(map(str, coins))  # save space when storing in used

    q = deque()
    q.append((coins, 0))
    used = set()
    used.add(store(coins))

    found = False
    while q:
        config, steps = q.popleft()
        # print(config)

        if config == end:  # is sorted
            print(steps)
            found = True

        for i in range(n):
            if not config[i]:  # nothing to move from here
                continue

            if i != 0 and (not config[i - 1] or config[i][-1] < config[i - 1][-1]):  # try moving left
                new_config = [i.copy() for i in config]
                to_move = new_config[i].pop()
                new_config[i - 1].append(to_move)  # move coin to the left

                temp = store(new_config)
                if temp not in used:
                    q.append((new_config, steps + 1))
                    used.add(temp)

            if i != n - 1 and (not config[i + 1] or config[i][-1] < config[i + 1][-1]):  # try moving right
                new_config = [i.copy() for i in config]
                to_move = new_config[i].pop()
                new_config[i + 1].append(to_move)  # move coin to the right

                temp = store(new_config)
                if temp not in used:
                    q.append((new_config, steps + 1))
                    used.add(temp)

    if not found:
        print("IMPOSSIBLE")
