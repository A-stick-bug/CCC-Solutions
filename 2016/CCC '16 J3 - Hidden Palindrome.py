A = input()
length = []
for i in range(len(A)):
    for j in range(i, len(A)):
        A2 = A[i:j + 1]
    if A2 == A2[::-1]:
        length.append(len(A2))
print(max(length))
