# brute force O(n), TLE
def find_gate(right):
    for i in reversed(range(right+1)):
        if not gates[i]:
            gates[i] = True
            return True
    return False


gates = [False for _ in range(int(input()))]  # False = no plane, True = occupied
n = int(input())
res = 0

for i in range(n):
    plane = int(input()) - 1
    if not find_gate(plane):  # couldn't find a gate to put plane
        break
    else:
        res += 1

print(res)
