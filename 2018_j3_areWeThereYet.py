x = input()
x = x.split()

first = int(x[0])
second = int(x[1])
third = int(x[2])
fourth = int(x[3])

print(f"0 {first} {first+second} {first+second+third} {first+second+third+fourth}")
print(f"{first} 0 {second} {second+third} {second+third+fourth}")
print(f"{first+second} {second} 0 {third} {third+fourth}")
print(f"{first+second+third} {second+third} {third} 0 {fourth}")
print(f"{first+second+third+fourth} {second+third+fourth} {third+fourth} {fourth} 0")