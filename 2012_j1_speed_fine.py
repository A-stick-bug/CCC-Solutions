limit = int(input())
speed = int(input())

if speed <= limit:
    print("Congratulations, you are within the speed limit!")
elif speed - 20 <= limit:
    print("You are speeding and your fine is $100.")
elif speed - 31 <= limit:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")
