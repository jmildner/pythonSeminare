print("Übung 1.4")

end_prize = 0
number = int(input("enter number of item (int)   > "))
prize = float(input("enter prize  of item (float) > "))

print(type(number), type(prize), type(end_prize))

end_prize = number * prize
print(number, "pieces", "at", prize, "$ cost", end_prize)

print(type(number), type(prize), type(end_prize))
