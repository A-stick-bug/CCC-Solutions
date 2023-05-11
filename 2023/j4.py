row_length = int(input())
row1 = input().split()
row2 = input().split()

tape = 0

if row1[0] == "1":
    tape += 3
for i in range(1, row_length):
    if row1[i] == "1":
        tape += 3
        if row1[i - 1] == "1":
            tape -= 2

# bottom row touches top row is index is EVEN
if row2[0] == "1":
    if row1[0] == "1":
        tape += 1
    else:
        tape += 3

for i in range(1, row_length):
    if row2[i] == "1":
        tape += 3
        if i % 2 == 0:  # check if touches top
            if row1[i] == "1":
                tape -= 2

        if row2[i - 1] == "1":
            tape -= 2

print(tape)
