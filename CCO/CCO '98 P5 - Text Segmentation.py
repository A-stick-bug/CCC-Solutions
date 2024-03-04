# https://dmoj.ca/problem/cco98p5
# Similar to https://leetcode.com/problems/word-break/
#
# goal: break a word into fewest words possible
# brute forcing each word with bfs will work due to low constraints and also guarantee
# that we use the least amount of words
#
# TC: no idea

from collections import deque

n = int(input())
words = [input() for _ in range(n)]


def word_break(s):
    q = deque([""])
    prev = {}  # keep track of previous word, so we can trace back the words we used
    while q:
        cur = q.popleft()

        if cur == s:  # found word
            used = []
            while cur != "":
                used.append(cur[len(prev[cur]):])
                cur = prev[cur]
            return used[::-1]

        for w in words:
            if s[len(cur):].startswith(w):
                new = cur + w
                if new in prev:
                    continue
                prev[new] = cur
                q.append(new)
    return -1


q = int(input())
for _ in range(q):
    s = input()
    ans = word_break(s)
    if ans != -1:
        print(" ".join(word_break(s)))
    else:
        print("***" + s)
