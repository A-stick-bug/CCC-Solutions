# O(n), where n is the radius of the circle

from math import floor

# pythagorean theorem using 1 side + hypotenuse
dist = lambda x: floor((r ** 2 - x ** 2) ** 0.5)

while True:
    r = int(input())
    if r == 0:
        break

    total = 0

    # find the amount of points inside the circle for 1 quadrant
    for i in range(r + 1):
        total += dist(i)

    print(total * 4 + 1)  # x4 to account for all 4 quadrants and +1 because for some reason my output is always 1 less
