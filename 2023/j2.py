peppers = {'Poblano': 1500,
           'Mirasol': 6000,
           'Serrano': 15500,
           'Cayenne': 40000,
           'Thai': 75000,
           'Habanero': 125000}

repeats = int(input())

count = 0

for i in range(repeats):
    add = input()
    count += peppers[add]

print(count)