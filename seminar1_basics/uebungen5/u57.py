print("Übung 5.7 - for loops")

for i in range(20): print(i, end=", ")  # von 0 bis excl. 20
print()

for i in range(50, 70): print(i, end=", ")  # von 50 bis excl. 70
print()

for i in range(3, 31, 3): print(i, end=", ")  # von 1 bis 30, step 3
print()

for ix, val in enumerate(range(665, 712, 5)):
    print(ix, "/", val, end=", ")
