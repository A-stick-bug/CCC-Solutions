# 70/100
# improved to O(N^2), might add full solution later

def solve():
    s = input()
    trie = {}

    def add_word(word):
        cur = trie
        for char in word:
            if char in cur:
                cur = cur[char]
            else:
                cur[char] = {}
                cur = cur[char]

    for i in range(len(s)):
        add_word(s[i:])

    tot = 0
    stack = [trie]
    while stack:
        cur = stack.pop()
        tot += 1
        for adj in cur.values():
            stack.append(adj)
    print(tot)


for _ in range(int(input())):
    solve()
