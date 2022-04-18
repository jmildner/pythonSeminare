print("Übung 3.3")

start = int(input("enter start   > "))
stop = int(input("enter stop    > "))
divider = int(input("enter divider > "))

for x in range(start, stop + 1):
    if x % divider == 0:
        print(x)
