# brute force solution (passes half the test cases)

for _ in range(int(input())):
    s = input()
    res = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            res.add(s[i:j])
    print(len(res)+1)
