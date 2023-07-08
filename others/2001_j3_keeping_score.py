deck = input()

def check_value(value):
    if 2 <= int(i) <= 9 or int == "T":
        return 0
    elif i == "J":
        return 1
    elif i == "Q":
        return 2
    elif i == "K":
        return 3
    elif int(i) == 1:
        return 4

list_deck = list(deck)
print(list_deck)
#c,d,h,s
for i in list_deck:
    if i == "C":
        suit = "club"
    elif i == "D":
        suit = "diamond"
    elif i == "H":
        suit = "heart"
    elif i == "S":
        suit = "spades"

