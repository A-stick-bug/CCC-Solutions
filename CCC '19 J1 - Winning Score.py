a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

total1 = a*3+b*2+c
total2 = d*3 + e*2 + f

if total1 == total2:
    print("T")
elif total1 > total2:
    print("A")
else:
    print("B")