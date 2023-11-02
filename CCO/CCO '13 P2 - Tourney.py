# Very interesting question, the 2D array I used for this question resembles a tree,
# but it's much more memory efficient than an actual tree using nodes
#
# - Question uses 1-indexing, so we convert to 0-indexing and use +1 when outputting
# - 1 << N = 2^N, but it's faster
#
# - get winner: O(1)
# - get wins of player: O(log(n))
# - switch player: O(log(n))

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ROUNDS = N  # there will be N rounds until winner is decided
N = 1 << N  # 2^n total people

skill = [int(input()) for _ in range(N)]
tourney = [[-1] * (N) for _ in range(ROUNDS + 1)]

for i in range(N):  # default values
    tourney[0][i] = i
for i in range(ROUNDS):
    for j in range(0, N // (1 << i), 2):
        # tourney[i][j] and tourney[i][j + 1] are competing in this round, winner moves on to the next
        if skill[tourney[i][j]] > skill[tourney[i][j + 1]]:
            tourney[i + 1][j // 2] = tourney[i][j]
        else:
            tourney[i + 1][j // 2] = tourney[i][j + 1]

for _ in range(M):
    q = input().split()
    if q[0] == "W":
        print(tourney[-1][0] + 1)  # get winner, 1-indexing

    elif q[0] == "S":  # see how many rounds player i won
        player = int(q[1]) - 1  # 0-indexing
        round = 0
        index = player
        while round <= ROUNDS and tourney[round][index] == player:  # go down the 'tourney tree' until player loses
            round += 1
            index //= 2
        print(round - 1)  # minus one because the person lost at round, so they won one less

    else:  # change a player's skill
        person, new_skill = map(int, q[1:])
        person -= 1  # 0-indexing
        skill[person] = new_skill

        # because this person's skill changed, the results of every round he participated in can also change
        # a person can only participate in log(N) rounds at most where N is the number of people
        j = person
        for i in range(ROUNDS):
            j = j // 2 * 2  # make number even, eg. 7 -> 6, 8 -> 8

            if skill[tourney[i][j]] > skill[tourney[i][j + 1]]:
                tourney[i + 1][j // 2] = tourney[i][j]
            else:
                tourney[i + 1][j // 2] = tourney[i][j + 1]
            j //= 2  # go to next round
