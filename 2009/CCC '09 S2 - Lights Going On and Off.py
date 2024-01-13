"""
Observation and implementation, using built in XOR

Notice the low constraints
- each row only has 8 lights, so 2^8=265 possible states
- O(R*2^L) will pass for sure

Even though we can press the buttons in any order, we only create new states from pressing them in increasing order
In other words, choose a subsequence of rows and press the buttons in that subsequence in order

"""

R = int(input())
L = int(input())
rows = [int(input().replace(" ", ""), 2) for _ in range(R)]  # convert to int to use built in XOR

possible = [set() for _ in range(R)]
possible[0] = {rows[0]}  # base case

for i in range(1, R):
    possible[i].add(rows[i])  # option 1: don't press button
    for prev in possible[i - 1]:
        possible[i].add(rows[i] ^ prev)  # option 2: xor with previous row

print(len(possible[-1]))
