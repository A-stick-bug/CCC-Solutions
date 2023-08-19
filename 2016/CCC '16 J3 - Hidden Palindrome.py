A = input()
length = []
for i in range(len(A)):
    for j in range(i, len(A)):
        A2 = A[i:j + 1]
    if A2 == A2[::-1]:
        length.append(len(A2))
print(max(length))

# O(n)
# def manacher(s):
#     t = '#'.join('^{}$'.format(s))
#     n = len(t)
#     p = [0] * n
#     c = r = 0
#     for i in range(1, n-1):
#         if r > i:
#             p[i] = min(r - i, p[2*c - i])
#         while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
#             p[i] += 1
#         if i + p[i] > r:
#             c, r = i, i + p[i]
#
#     max_len, center_index = max((p[i], i) for i in range(1, n-1))
#     start_index = (center_index - max_len) // 2
#     return len(s[start_index: start_index + max_len])
#
# print(manacher(input()))
