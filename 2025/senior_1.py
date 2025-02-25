a, b, c, d = map(int, input().split())

ans1 = (a + c) + max(d, b)
ans2 = (b + d) + max(a, c)
print(min(ans1, ans2) * 2)
