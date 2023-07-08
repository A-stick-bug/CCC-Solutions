packages = int(input())
collisions = int(input())

point = 0

if packages > collisions:
    point += 500

print(packages*50 - collisions*10 + point)
