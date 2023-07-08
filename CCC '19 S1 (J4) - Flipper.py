# brute force passes all test cases

flip = input()

square = [1, 2, 3, 4]

for i in flip:
    if i == "H":
        square[0], square[1], square[2], square[3] = square[2], square[3], square[0], square[1]
    else:
        square[0], square[1], square[2], square[3] = square[1], square[0], square[3], square[2]

print(square[0], square[1])
print(square[2], square[3])
